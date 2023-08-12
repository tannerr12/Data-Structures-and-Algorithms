class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
                
        
        def lcs(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]
        
        word = lcs(str1,str2)
        idx1,idx2 = 0,0
        ans = ''
        for c in word:
            
            while idx1 < len(str1) and str1[idx1] != c:
                ans += str1[idx1]
                idx1 += 1
            while idx2 < len(str2) and str2[idx2] != c:
                ans += str2[idx2]
                idx2 += 1
            
            ans += c
            idx1 += 1
            idx2 += 1
        
        
        ans += str1[idx1:]
        ans += str2[idx2:]
        
        return ans