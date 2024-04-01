class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        
        adj = defaultdict(list)
   
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        

        best = {}
        def dfs2(node,par):
            
            res = coins[node]
            
            for edge in adj[node]:
                if edge == par:
                    continue
                res = max(res,coins[node], dfs2(edge, node))
            
            best[node] = res
            return res
        
        dfs2(0,-1)
        
        @cache
        def dfs(node,par,mult):
            
            res = 0
            if mult >= 14 or best[node] >> mult == 0:
                return res
            
            for edge in adj[node]:
                if edge == par:
                    continue
                
                cur = float('-inf')
                
                #Option 1
                cur = max(cur,dfs(edge,node, mult) + (coins[edge] >> (mult)) - k)
                
                #Option 2
                if mult < 14:
                    cur = max(cur,dfs(edge,node, mult + 1) + (coins[edge] >> ((mult + 1))))
                
                res += cur
            
            return res
        
        
        res = float('-inf')
        #Option 1
        res = max(res, dfs(0,-1, 0) + coins[0] - k)

        #Option 2
        res = max(res, dfs(0,-1, 1) + (coins[0] >> (0 + 1)))

        

        
        
        
        return res
            