class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        print(dp)
        for i in range(n):
            dp[i][i] = piles[i]

        for r in range(1,n):
            for i in range(n - r):
               dp[i][i+r] = max(piles[i] - dp[i+1][i+r], piles[i + r] - dp[i][i+r -1])


        return dp[0][-1]> 0