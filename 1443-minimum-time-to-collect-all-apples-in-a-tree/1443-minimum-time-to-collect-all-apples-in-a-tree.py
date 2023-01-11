class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
            
        adj= defaultdict(list)
        
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        
    
        
        def dfs(child,parent):
            if len(adj[child]) ==0:
                return False,0
            
            total = 0
            for e in adj[child]:
                if e == parent:
                    continue
                    
                r,c = dfs(e,child)
                
                if r:
                    total += c
            
            
            if total > 0 or hasApple[child]:
                return True, total + 2
            else:
                return False, 0
        
        
        
        r, res = dfs(0,-1)
        
        
        if r:
            res -=2
        
        return res
        
    
            
            
            