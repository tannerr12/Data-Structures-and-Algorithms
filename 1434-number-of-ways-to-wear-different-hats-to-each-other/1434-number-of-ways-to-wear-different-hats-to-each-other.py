class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:

        possibleHats = defaultdict(set)
        for i in range(len(hats)):
            for h in hats[i]:
                possibleHats[h].add(i)
        
        
        MOD = 10 ** 9 + 7
        ph = list(possibleHats)
       
        @cache
        def dfs(mask,hatId):
            
            if mask == 2 ** len(hats) -1:
                return 1
            
            res = 0
            
            for i in range(hatId, len(ph)):
                for p in possibleHats[ph[i]]:
                    if mask & (1 << p) > 0:
                        continue
                    res += dfs(mask | (1 << p),i+1)
                    res %= MOD
        
            return res % MOD
        
        
        return dfs(0,0) % MOD
            
            
            
            
                
                
                
        
            
            