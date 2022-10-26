class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        h = {0:0}
        
        s = 0
        
        for i in range(len(nums)):
            
            s += nums[i]
            
            if s % k not in h:
                h[s%k] = i +1
            elif i - h[s%k] >= 1:
                return True
            
        
        return False
                
                
                
                
            
             
            