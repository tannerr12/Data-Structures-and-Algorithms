class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        res = float('inf')
        l = 0
        total = 0
        for i in range(len(nums)):
            
            val = nums[i]
            
            total += val
            
            if total >= target:
                while total >= target:
                    res = min(i+1 - l, res)
                    total -= nums[l]
                    l+=1
                    
                    
        
        
        
        return res if res != float('inf') else 0
            
            
            