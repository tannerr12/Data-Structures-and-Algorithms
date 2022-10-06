class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = {}
        def dfs(l,r):
            
            if l > r: return 0
            if r == l: return 1
            
            if (l,r) in dp:
                return dp[(l,r)]
            
            
            if s[l] == s[r]:
                dp[(l,r)] = dfs(l+1,r-1) + 2
                return dp[(l,r)]
            
            
            
            dp[(l,r)] = max(dfs(l+1,r), dfs(l,r-1))
            return dp[(l,r)]
        
        return dfs(0,len(s) -1)
            