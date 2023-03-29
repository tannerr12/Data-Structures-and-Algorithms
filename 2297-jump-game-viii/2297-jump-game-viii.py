class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:


        iStack = []
        dStack = []
        
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i,num in enumerate(nums):
            
            while iStack and num < nums[iStack[-1]]:
                idx = iStack.pop()
                dp[i] = min(dp[i], dp[idx] + costs[i])
            
            while dStack and num >= nums[dStack[-1]]:
                idx = dStack.pop()
                dp[i] = min(dp[i], dp[idx] + costs[i])
            
            iStack.append(i)
            dStack.append(i)
        
        
        return dp[-1]
                
        