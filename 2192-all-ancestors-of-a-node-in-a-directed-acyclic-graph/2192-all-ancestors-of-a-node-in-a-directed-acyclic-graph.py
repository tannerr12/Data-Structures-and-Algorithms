class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adj = defaultdict(list)
        res = [set() for _ in range(n)]
        
        for i in range(len(edges)):
            
            x,y = edges[i]
            adj[y].append(x)
            
        
        
        #print(adj)
        
        
        parent = defaultdict(list)
        
       
        @cache
        def dfs(i):
            
            seen = set([i])
            for x in adj[i]:
                for y in dfs(x):
                    seen.add(y)
                
                
                
            return seen
        
        
        
        
        for key in range(n):
            
            res[key] = set(dfs(key))
            res[key].remove(key)
        
       
        
        
        
      
        
        
        for i in range(n):
            
            res[i] =list(sorted(res[i]))
            
            
                
        
        
        return res
        
            
            
            
        
            
        
        