class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
         #DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
            
            
            dp = [[0 for i in range(len(text2) +1)] for j in range(len(text1) +1)]
            
            print(dp)
            for i in range(1,len(text1) +1):
                
                for j in range(1,len(text2) +1):
                    
                    if text1[i -1] == text2[j -1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
            
            return dp[-1][-1]