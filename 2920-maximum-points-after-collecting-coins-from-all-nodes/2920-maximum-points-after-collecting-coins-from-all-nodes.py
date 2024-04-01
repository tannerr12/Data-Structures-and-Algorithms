class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        
        adj = defaultdict(list)
        parents = defaultdict(int)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        
        def dfs2(node,par):
            
            parents[node] = par
            for edge in adj[node]:
                if edge != par:
                    dfs2(edge,node)
        
        dfs2(0,-1)
        #print(parents)
        
        @cache
        def dfs(node,mult):
            
            #if len(adj[node]) == 1 and adj[node][0] == par:
            #    return 0
            
            res = 0
            if mult >= 14:
                return res
            
            for edge in adj[node]:
                if edge == parents[node]:
                    continue
                
                cur = float('-inf')
                #Option 1
                cur = max(cur, dfs(edge, mult) + (coins[edge] >> (mult)) - k)
                
                #Option 2
                if mult < 14:
                    cur = max(cur, dfs(edge, mult + 1) + (coins[edge] >> ((mult + 1))))
                
                res += cur
            
            return res
        
        
        res = float('-inf')
        #Option 1
        res = max(res, dfs(0, 0) + coins[0] - k)

        #Option 2
        res = max(res, dfs(0, 1) + (coins[0] >> (0 + 1)))

        

        
        
        
        return res
            