class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        
        MOD = 10 ** 9 + 7
        
        @cache
        def dfs(m, i, p):
            
            if i >= len(profit):
                
                if p >= minProfit:
                    return 1
                else:
                    return 0
            
            res = 0
            #skip this crime
            res += dfs(m,i+1,p) % MOD
            res %= MOD
            #take this crime
            if m >= group[i]:
                updatedProfit = p + profit[i] if p + profit[i] < minProfit else minProfit
                res += dfs(m - group[i], i+1, updatedProfit) % MOD
                res %= MOD
                
            return res % MOD
        
        
        return dfs(n, 0, 0) % MOD
    
        
            