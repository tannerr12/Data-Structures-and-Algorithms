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
            if hatId >= len(ph):
                return 0
            res = 0
            
            res += dfs(mask,hatId+1)
            
            for p in possibleHats[ph[hatId]]:
                if mask & (1 << p) > 0:
                    continue
                res += dfs(mask | (1 << p),hatId+1)
                res %= MOD

            return res % MOD
        
        
        return dfs(0,0) % MOD
            
            
            
            
                
                
                
        
            
            