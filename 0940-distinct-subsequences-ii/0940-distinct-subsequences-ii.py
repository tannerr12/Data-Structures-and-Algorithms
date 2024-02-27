class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(i):
            
            if i >= len(s):
                return 1
            
            if i == -1:
                res = 0
            else:
                res = 1
            
            seen = set()
            
            for j in range(i+1, len(s)):
                if s[j] not in seen:
                    res += dfs(j) % MOD
                    res %= MOD
                    seen.add(s[j])
            
            return res
        
        
        
        return dfs(-1)
            
                