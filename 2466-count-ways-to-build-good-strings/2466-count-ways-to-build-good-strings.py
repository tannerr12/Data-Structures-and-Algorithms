class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
            modulo = 10 ** 9 + 7
            dp = [1] + [0] * high


            for k in range(1,high+1):
                dp[k] = dp[k - zero] + dp[k- one]
                dp[k] = dp[k] % modulo


            return sum(dp[low:]) % modulo
            