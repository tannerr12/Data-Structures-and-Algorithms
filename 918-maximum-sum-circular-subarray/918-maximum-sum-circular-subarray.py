class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
     
        maxSum = float('-inf')
        currSum = float('-inf')
        for i in range(len(nums)):
            currSum += nums[i]
            
            currSum = max(currSum,nums[i])
            
            maxSum = max(currSum,maxSum)
            
        
        
        leftsum = [0] * len(nums)
        
        leftMax = [0] * len(nums)
        
        rightSum = [0] * len(nums)
        
        currleft = 0
        for i in range(len(nums) -1,-1,-1):
            currleft += nums[i]
            
            leftsum[i] = currleft

            
        currMax = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            
            currMax = max(currMax, leftsum[i])
            
            leftMax[i]= currMax
        
        currRight = 0
        for i in range(len(nums)):
            currRight += nums[i]
            
            rightSum[i] = currRight

            
        currMax2,maxSum2 = float('-inf'),float('-inf')
        for i in range(len(nums)-1):
            
            currMax2 = max(currMax2, rightSum[i] + leftMax[i+1])
            
            maxSum2= max(currMax2, maxSum2)
        
            
            
        
        
        return max(maxSum2,maxSum)