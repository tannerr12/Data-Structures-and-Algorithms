from sortedcontainers import SortedList
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        '''
        res = 0
        
        for i,v in enumerate(nums):
            nums[i] = [v,i]
            
        sl = SortedList()
        nums.sort()
        
        stack = []
        last = -1
        for v,i in nums:
            if v != last:
                while stack:
                    idxx = stack.pop()
                    sl.add(idxx)
            
            idx = bisect_right(sl, i)
            
            left = idx 
            right = len(sl) - (idx)
            
            if left >=k and right >= k:
                res +=1
                
            stack.append(i)
            last = v
            
        return res
    
        '''
        
        heap = []
        left = [0] * len(nums)
        res = 0
        
        for i,v in enumerate(nums):
            
            if len(heap) == k and -heap[0] < v:
                left[i] = True
            
            heappush(heap, -v)
            
            if len(heap) > k:
                heappop(heap)
                
        
        heap = []
        
        for i in range(len(nums)-1,-1,-1):
            
            if left[i] and len(heap) == k and -heap[0] < nums[i]:
                res +=1
            
            heappush(heap, -nums[i])
            
            if len(heap) > k:
                heappop(heap)
        
        
        return res
        