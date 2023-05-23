class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        adj = defaultdict(list)
        
        for x,y in edges:
            adj[x].append(y)
            if x == y and x == destination:
                return False
            
        dp = [None] * n    
        
        def dfs(node):
            
            if len(adj[node]) == 0:
                return node == destination
            
            if dp[node] != None:
                return dp[node]
            
            dp[node] = False
            for x in adj[node]:
                if not dfs(x):
                    return False
                
            dp[node] = True
            return True
            
            
        return dfs(source)
        
            
            
            
            
            
            
            