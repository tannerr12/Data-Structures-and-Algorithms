class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0

        prefix = [0]
        
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        dp = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            left = 0
            if stack:
                left = stack[-1] +1
            
            dp[i] += prefix[i] - prefix[left]
            stack.append(i)
        
        
       
        stack = []        
        for i in range(len(nums)-1,-1,-1):
            
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            right = len(nums)
            if stack:
                right = stack[-1] 

            dp[i] += (prefix[right] - prefix[i]) 
            res = max(res, dp[i] * nums[i])
            stack.append(i)
                
        
        return res % MOD
        