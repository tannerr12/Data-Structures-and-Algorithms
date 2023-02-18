class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        
        adj = defaultdict(list)
        
        for x,y in connections:
            
            adj[x].append([y,0])
            adj[y].append([x,1])
        
        
   
        res = 0
        def dfs(i,par):
            nonlocal res

            for key,c in adj[i]:
                if key == par:
                    continue
                res += c
                dfs(key,i)
            
            
           
        
        dfs(0,-1)
        
        return n - res -1