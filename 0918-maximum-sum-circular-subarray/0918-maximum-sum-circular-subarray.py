class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
      
        total = 0
        maxSum = nums[0]
        curMax = 0
        minSum = nums[0]
        curMin = 0
        
        for i in range(len(nums)):
            n = nums[i]
            
            
            #max pass
            curMax = max(curMax + n, n)
            maxSum = max(maxSum, curMax)
            
            #minPass
            curMin = min(curMin + n, n)
            minSum = min(curMin,minSum)
            
            #sum of all
            total += n
        #max sub array found, or the total - the smallest found
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum