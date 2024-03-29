class Solution:
    def distinctSubseqII(self, s: str) -> int:
                
        MOD = 10 ** 9 + 7
        mp = defaultdict(list)
        for i in range(len(s)):
            num = ord(s[i]) - ord('a')
            mp[num].append(i)
        
        @cache
        def dfs(i):
            
            res = i != -1

            for j in range(26):
                
                idx = bisect_right(mp[j], i)
                
                if idx >= len(mp[j]):
                    continue
                    
                res += dfs(mp[j][idx]) % MOD
                res %= MOD

            
            return res
        
        
        
        return dfs(-1)
            
                