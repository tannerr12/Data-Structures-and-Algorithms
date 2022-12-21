class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        
        
        adj = defaultdict(list)
        seen = set()
        colordct = {}
        for x,y in dislikes:
            
            
            adj[x].append(y)
            adj[y].append(x)
            
            
        
        
        
       # print(npossible)
        
        
        seen = set()
        for i in range(1,n +1):
            if i in seen:
                continue
            
            q = deque()
            q.append(i)
            colordct[i] = False
            while q:

                for i in range(len(q)):
                    node = q.popleft()
                    

                    for x in adj[node]:
                    
                        if x in colordct:
                            if colordct[x] ==colordct[node]:
                                return False
                        else:
                            colordct[x] = not colordct[node]
                            
                            q.append(x)
                            seen.add(x)

        
                
        return True
                    