class Solution:
    def minInsertions(self, s: str) -> int:
        
        @cache
        def dfs(l,r):
            
            if l > r:
                return 0
            res = 0
            if s[l] == s[r]:
                if l == r:
                    return 1
                res = max(res,dfs(l+1,r-1) + 2)
            
            else:
                #try left
                res = max(res, dfs(l+1,r))
                #try right
                res = max(res,dfs(l,r-1))
            
            
            return res
        
        res = dfs(0,len(s)-1)
        
        return len(s) - res