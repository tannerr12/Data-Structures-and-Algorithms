class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i, f):
            
            if f == 0:
                return i == finish
            
            res = 0
            
            for j in range(len(locations)):
                if j == i:
                    continue
                    
                if abs(locations[i] - locations[j]) <= f:
                    res += dfs(j, f - abs(locations[i] - locations[j]))
                    res %= MOD
            
            return res + (i == finish)
        
        
        return dfs(start, fuel) % MOD
    
    