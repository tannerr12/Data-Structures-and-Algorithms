class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        
        #if increase readjust 2,3 we take 3 
        #if decrease we take min 2,3,2,1,2 #buy at 3 sell at 1 than buy at 2 again
        
        ans = 0
        cur = 0
        
        high = 0
        low = float('inf')
        for i in range(len(nums)):
            
            low = min(low,nums[i])
            
            if nums[i] > low:
                ans += high - low
                high = nums[i]
                low = nums[i]
            high = max(high, nums[i])
            
        
        
        return ans + high
        