class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        pows = set()
        for i in range(16):
            pows.add(5 ** i)
        
        @cache
        def dfs(i, val):
            
            if i >= len(s):
                if val > 0 and val not in pows:
                    return float('inf')
                elif val in pows:
                    return 1
                return 0
            
            res = float('inf')
            #take this
            if val in pows:
                res = min(res, dfs(i, 0) + 1)
            
            
            #leave this
            if not (s[i] == '0' and val == 0):
                if s[i] == '1':
                    res = min(res, dfs(i+1, (val << 1) ^ 1))
                else:
                    res = min(res, dfs(i+1, (val << 1)))
            
            return res
        
        
        if s[0] == '0':
            return -1
        
        ans = dfs(1,1)
        
        return ans if ans != float('inf') else -1