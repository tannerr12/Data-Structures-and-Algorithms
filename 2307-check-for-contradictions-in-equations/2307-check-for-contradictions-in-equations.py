class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        
        def checkDiff(a,b):
            return abs(a-b) > 10**-5
            
        adj = defaultdict(set)
        
        for (x,y), i in zip(equations, values):
            
            adj[x].add((y, i))
            adj[y].add((x, 1/i))
            
            
        values = {}
        def dfs(node):
            
            for n,val in adj[node]:
                if n in values:
                    if checkDiff(values[node] / val, values[n]):
                        return True
                else:
                    values[n] = values[node] / val
                    if dfs(n):
                        return True
                
            
            
            return False
        
        
        for key in adj:
            if key not in values:
                values[key] = 1
            if dfs(key):
                return True
            
        
        return False
            
                    
                    
                    
                    
                    
                    
        
            
                
        
        
        