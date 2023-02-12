class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
   
        
        adj = defaultdict(list)
        
        for x,y in roads:
            adj[x].append(y)
            adj[y].append(x)
        
        res = 0
        #seen = set()
        def dfs(x,parent):
            nonlocal res
            total = 0   
            #dp[x] = min(dp[x], math.ceil(depth / seats))
            for y in adj[x]:
                if y != parent:
                    c = dfs(y, x)
                    res += math.ceil(c / seats)
                    total += c
            
            return total +1
        
        dfs(0,-1)
        return res
            
            
            
        
        