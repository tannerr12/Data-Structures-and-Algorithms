class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        
        adj = defaultdict(list)
        N = len(edges) +1
        
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
        
    
        lookup = set()
        for x,y in guesses:
            
            lookup.add((x,y))
            
        
        g = [0] * N
        
        
        #returns the number of guesses that are down tree from node 0 for each node
    
        def go(node,parent):
            r = 0
            for v in adj[node]:
                if parent != v:
                    if (node,v) in lookup:
                        r +=1
                    r += go(v,node)
                    
                
            g[node] += r
            return r
        
        #count = the number of against current edges for each node "up tree"
        
        def go2(node,parent,counts):
            
            for v in adj[node]:
                if parent != v:
                    c = counts
                    if (v,node) in lookup:
                        c+=1
                    if (node,v) in lookup:
                        c-=1
                    go2(v,node,c+ g[node] - g[v])
            g[node] += counts
        
        
        go(0,-1)
        go2(0,-1,0)
        count = 0
        
        for i in range(N):
            if g[i] >= k:
                count +=1
        return count