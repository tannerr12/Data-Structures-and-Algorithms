class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        
        seen = set()
        
        res = 0
        for i in range(len(nums)):
            
            if i in seen:
                continue
                
            temp = 0
            
            val = i
            while nums[val] >= 0 and nums[val] < len(nums) and val not in seen:
                
                temp +=1
                seen.add(val)
                val = nums[val]
                
            
            
            res = max(temp,res)
            
        
        
        return res
            