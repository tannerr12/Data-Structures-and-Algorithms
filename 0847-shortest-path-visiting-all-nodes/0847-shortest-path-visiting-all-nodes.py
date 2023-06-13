class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        m = 2 ** len(graph)
        m -= 1
        #print(m)
        seen = set()
        N = len(graph)
        dist = [[float('inf')] * N for _ in range(N)]
        
        for i, edges in enumerate(graph):
            dist[i][i] = 0
            for edge in edges:
                dist[i][edge] = 1
        
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        @cache
        def visit(node,mask):
            nonlocal m
            if mask == m:
                return 0
            
            res = float('inf')
            for i in range(N):
                
                if mask & (1 << i) == 0:
                    res = min(res, visit(i, (1 << i) | mask) + dist[node][i])
            
            return res
        
        
        res = float('inf')
        
        for i in range(N):
            res = min(res, visit(i,(1 << i)))
        
                      
        return res
