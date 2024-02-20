class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        adj = defaultdict(list)
        
        for x,y,z in edges:
            adj[x].append((y, z))
            adj[y].append((x, z))
        
        seen = defaultdict(int)
        seen[0] += 1
        mx = 0
        def dfs(node, time, score):
            
            
            best = 0
            
            #try an existing branch
            for child,cost in adj[node]:
                nonlocal mx
                if time < cost:
                    continue
                
                seen[child] += 1   
                if seen[child] == 1:
                    best = max(best,dfs(child, time - cost, score + values[child]))
                else:
                    best = max(best,dfs(child, time - cost, score))  
                    
                seen[child] -= 1
            
            if node == 0:
                mx = max(mx,score) 
            return 0
        
        
        dfs(0, maxTime,values[0])
        
        return mx
            
                