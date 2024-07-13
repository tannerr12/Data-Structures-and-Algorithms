class Solution:
    def numWays(self, s: str) -> int:
        
        MOD = 10**9 + 7
        cur = 0
        mp = defaultdict(int)
        
        for val in s:
            if val == '1':
                cur += 1
                
            mp[cur] += 1
        
        
        if cur == 0:
            n = len(s)
            if n < 3:
                return 0
            return ((n - 1) * (n - 2) // 2) % MOD
        
        
        if cur % 3:
            return 0
        
        target = cur // 3
        res=0
        res += ((mp[target] % MOD) * (mp[target * 2] % MOD)) % MOD
        
        return res % MOD
        
            
        