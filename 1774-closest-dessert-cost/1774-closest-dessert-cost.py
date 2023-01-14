class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        results = float('inf')
        
        @cache
        def dfs(i,j,res):
            nonlocal results
            if j >= len(toppingCosts):
                res += baseCosts[i]
                if abs(res - target) <= abs(results - target):
                    if abs(res - target) == abs(results - target):
                        results = min(res,results)
                    else:
                        results = res 
                return 0
            
            
            #take 1
            dfs(i, j+1,res + toppingCosts[j]) 
            #take 2
            dfs(i,j+1,res + (toppingCosts[j] * 2))
            #dontTake
            dfs(i, j+1, res)

     
        
        
        for i in range(len(baseCosts)):
            
            dfs(i, 0, 0)
        
        
        
        return results