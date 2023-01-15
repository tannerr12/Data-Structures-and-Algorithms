class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0

        local = 1
        g = 1
        prev = nums[0]
        for i in range(1,len(nums)):

            k -= abs(prev - nums[i]) * (i-l)
            
            prev = nums[i]
            while k < 0:
                k += abs(nums[l] - nums[i])
                l+=1
     
            g = max(g, (i+1 - l))
            
        
        
        return g