class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        """        
        heap = []
        
        keys = Counter(nums)
        
        for key,val in keys.items():
            
            heappush(heap, (-key,val))
        
        
        res = 0
        while len(heap) > 1:
            
            val,size = heappop(heap)
            
            nxtVal,nxtSize = heappop(heap)
            
            res += size
            
            heappush(heap,(nxtVal, size + nxtSize))
            
        
        return res
            
        """
        
        res = 0
        nums.sort()
        
        unique = set()
        for i in range(len(nums)):
            unique.add(nums[i])
            res += len(unique) -1
                
        return res
            
            