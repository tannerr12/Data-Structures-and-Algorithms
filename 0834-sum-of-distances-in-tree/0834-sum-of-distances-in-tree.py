class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        adj = defaultdict(list)
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
            
            
        
        dp = [0] * n
        count = [1] * n
        seen =set()
        def dfs(root,parent):
            
            for child in adj[root]:
                if child != parent:
                    dfs(child,root)
                    count[root] += count[child]
                    dp[root] += dp[child] + count[child]
                    
                
                
            
        
        
        def dfs2(root,parent):
            for child in adj[root]:
                if child != parent:
                    dp[child] = dp[root] - count[child] + n - count[child]
                    dfs2(child,root)
        dfs(0,None)
        dfs2(0,None)
        
        return dp