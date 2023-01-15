class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        local = 0 
        g = 0
        
        for i in range(len(nums)):
            
            prev = local & nums[i]
            
            #if prev == 0:
              #  local ^= nums[i]
            
            while prev != 0:
                
                local ^= nums[l]
                l+=1
                prev = local & nums[i]
            
            local ^= nums[i]
            
            g = max(g, (i - l) + 1)
            
        
        
        return g
            