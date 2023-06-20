class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indeg = defaultdict(int)
        for x,y in adjacentPairs:
            adj[x].append(y)
            adj[y].append(x)
            indeg[y] +=1
            indeg[x] +=1
        
        
        q = deque()
        for key,val in indeg.items():
            if val == 1:
                q.append(key)
                break
                
        
        res = []
        seen = set()
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                if node in seen:
                    continue
                    
                res.append(node)
                seen.add(node)
                for x in adj[node]:
                    
                    indeg[x] -=1
                    
                    if indeg[x] <= 1:
                        q.append(x)
                    
                
        
        return res
            
        
        
        
            
        
        