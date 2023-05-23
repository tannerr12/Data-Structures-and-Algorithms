class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        adj = defaultdict(list)
        
        for x,y in edges:
            adj[x].append(y)
            if x == y and x == destination:
                return False
            
        dp = [None] * n    
        seen = set()
        def dfs(node):
            
            if len(adj[node]) == 0 and node == destination:
                return True
            
            if dp[node] != None:
                return dp[node]
            if node in seen and dp[node] == None:
                return False
            
            seen.add(node)
            res = False
            for x in adj[node]:
                val = dfs(x)
                if val == False:
                    return False
                else:
                    res = True
            
            dp[node] = res
            return res
            
            
        return dfs(source)
        
            
            
            
            
            
            
            