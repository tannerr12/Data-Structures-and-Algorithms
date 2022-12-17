class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        

        dp = [0 for i in range(len(nums))]
        stack = []
        for i in range(len(nums)-1,-1,-1):
            
            
            while stack and stack[-1][1] < nums[i]:
                idx,val = stack.pop()
                dp[i] = max(dp[i] +1, dp[idx])
                
            stack.append([i,nums[i]])
            
        
        
        return max(dp)