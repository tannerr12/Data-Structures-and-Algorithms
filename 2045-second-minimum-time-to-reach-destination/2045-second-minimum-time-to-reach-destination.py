class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        adj = defaultdict(list)
        
        for x,y in edges:
            
            adj[x].append(y)
            adj[y].append(x)
            
        
        heap = [[0, 1]]
        seen = defaultdict(lambda:[float('inf'),float('inf')])
        seen[1][0] = time
        #best = -1
        
        while heap:
            
            t,node = heappop(heap)       
            wait = change - t % change if ((t // change) % 2) else 0
            for v in adj[node]:
                
                if seen[v][0] > t + wait + time or seen[v][1] > t + wait + time:
                    if seen[v][0] >= t + wait + time:
                        seen[v][0] = t + wait + time
                    else:
                        seen[v][1] = t + wait + time
                        if v == n:
                            return seen[v][1]
                    
                    heappush(heap, [t + wait + time,v])

        
        
        