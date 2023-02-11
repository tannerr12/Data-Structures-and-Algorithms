class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        
        adj = defaultdict(list)
        
        for rx,ry in redEdges:
            adj[rx].append([ry, 1])
            
        for bx, by in blueEdges:
            adj[bx].append([by,0])
        
        
        res = [float('inf')] * n
        
        seen = set()
        
        q = deque()
        q.append([0,1])
        q.append([0,-1])
        
        level = 0
        
        while q:
            
            for i in range(len(q)):
                
                v,c = q.popleft()
                seen.add((v,c))
                res[v] = min(res[v], level)
                for x,col in adj[v]:
                    if col != c and (x,col) not in seen:
                        q.append([x,col])
                
            level +=1
        
        
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] = -1
                
        return res
            