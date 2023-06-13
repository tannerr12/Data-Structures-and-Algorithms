class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        m = 2 ** len(graph)
        m -= 1
        res = float('inf')
        for node in range(len(graph)):
            
            q = deque([[node,(1 << node)]])
            dp = {}
            level = 0
            while q:
                
                for i in range(len(q)):
                    
                    n, mask = q.popleft()
                    
                    if (n,mask) in dp:
                        continue
                    
                    if mask == m:
                        dp[(n,mask)] = level
                        res = min(res, level)
                        continue
                    
                    dp[(n,mask)] = level
                    
                    for val in graph[n]:
                        
                        q.append((val, mask | (1 << val)))
                
                level +=1
        
        return res
            
            
            