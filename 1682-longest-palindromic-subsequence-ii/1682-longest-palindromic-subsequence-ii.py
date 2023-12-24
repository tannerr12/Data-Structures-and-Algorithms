class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        @cache
        def dfs(i,j,lasti):
            
            if i >= j:
                return 0

            res = 0
            

            v = ord(s[i]) - ord('a')
            #shift both
            if (lasti != v) and s[i] == s[j]:
                
                res = max(res, dfs(i+1,j-1, v) + 2) 
            else:
                #shift left
                res = max(res, dfs(i+1, j, lasti))
                #shift right
                res = max(res, dfs(i, j-1, lasti))
            
            return res
        
        
        return dfs(0, len(s) -1, -1)