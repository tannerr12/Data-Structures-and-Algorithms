class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        
        heap = []
        
        
        l,r = 0,0
        m,n = len(nums1), len(nums2)
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if heap and (nums2[j] + nums1[i]) * -1 < heap[0][0] and len(heap) == k:
                    break
                heapq.heappush(heap, ((nums2[j] + nums1[i]) * -1, nums1[i], nums2[j]))
                
                if len(heap) > k:
                    heapq.heappop(heap)
        
        
        #print(heap)
        res = []
        while k and heap:
            
            x,y,z = heapq.heappop(heap)
            
            res.append([y,z])
            
            k-=1
        
        
        return res
            