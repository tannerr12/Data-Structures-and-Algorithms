class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        def CountSort(comp):
            
            count = [0] * 10
            
            for val in nums:
                v = (val // comp) % 10
                count[v] +=1
                
            
            idx = 0
            for i,e in enumerate(count):
                
                count[i] = idx
                idx += e
            
            ls = [0] * len(nums)
            for i,e in enumerate(nums):
                v = (e // comp) % 10
                ls[count[v]] = e
                
                count[v] +=1
                
            
            for i,e in enumerate(ls):
                nums[i] = e
            
            
        
        comp = 1
        for i in range(10):
            
            CountSort(comp)
            comp *= 10
            
        
        res = 0
        for i in range(1, len(nums)):
            res = max(nums[i]-nums[i-1], res)
            
        
        return res