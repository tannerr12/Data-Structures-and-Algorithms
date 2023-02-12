class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        s = sum(nums)
        dp = [[0 for j in range(2 * s + 1)] for i in range(len(nums))]

        dp[0][nums[0] + s] = 1
        dp[0][-nums[0] + s] += 1
        for i in range(1, len(nums)):
            for j in range(-s, s+1):
                if dp[i-1][j + s] > 0:
                    dp[i][j + nums[i] + s] += dp[i-1][j + s]
                    dp[i][j - nums[i] + s] += dp[i-1][j + s]


        return 0 if abs(target) > s else dp[len(nums) -1][target + s]     

                 
    