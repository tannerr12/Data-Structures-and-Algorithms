class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        
        adj = defaultdict(list)
        
        for x,y in edges:    
            adj[x].append(y)
            adj[y].append(x)
        
        
        
        
        def dfs(node, par):
            
            if node is None:
                return [0,0,-1]
            
            count = 0
            res = 0    
            same = True
            for val in adj[node]:
                if val == par:
                    continue
                
                countVal,best,col = dfs(val, node)
                count += countVal
                if col != colors[node]:
                    same = False
                res = max(res, best)
            
            return [count + 1 if same else 0, max(res , count + 1 if same else 0), colors[node] if same else 100]
        
    
    
        return dfs(0, -1)[1]
            
        