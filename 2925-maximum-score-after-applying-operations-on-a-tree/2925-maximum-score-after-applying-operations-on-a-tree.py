class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        adj = defaultdict(list)
        total = sum(values)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        def dfs(node,par):
            if len(adj[node]) == 0 or (len(adj[node]) == 1 and adj[node][0] == par):
                return values[node]
            
            val = 0
            for branch in adj[node]:
                if branch == par:
                    continue
                    
                val += dfs(branch, node)
            
            
            return min(val, values[node])
            
        
        return total - dfs(0,-1)
    
    
    #0 -> 1
    #2 ,  1