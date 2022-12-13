class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        h = Counter(arr)
        
        heap = []
        
        for key,val in h.items():
            
            heapq.heappush(heap, (-val,key))
            
        
        
        
        size = len(arr)
        res = 0
        while size > len(arr) //2:
            
            v, k = heapq.heappop(heap)
            
            res +=1
            size += v
        
        
        return res
            
        