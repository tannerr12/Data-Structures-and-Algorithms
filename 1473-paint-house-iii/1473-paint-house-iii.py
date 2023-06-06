class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        @cache
        def dfs(i, last, neigh):
            
            if i >= len(houses):
                if neigh == target:
                    return 0
                else:
                    return float('inf')
            res = float('inf')
            if houses[i] > 0:
                if houses[i]-1 == last:
                    res = min(res, dfs(i+1,houses[i] -1,neigh))
                else:
                    res = min(res, dfs(i+1,houses[i] -1,neigh + 1))
            else:
                for j in range(n):

                    if j == last:
                        res = min(res, dfs(i+1,j,neigh) + cost[i][j])

                    else:
                        res = min(res, dfs(i+1,j,neigh + 1) + cost[i][j])

            return res
        
        ans = dfs(0,-1, 0)
            
        return ans if ans != float('inf') else -1
                
                
            