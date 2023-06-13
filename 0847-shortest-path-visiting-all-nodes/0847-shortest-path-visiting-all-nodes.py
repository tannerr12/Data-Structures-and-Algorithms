class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        m = 2 ** len(graph)
        m -= 1
        print(m)
        dp = {}
        '''
        def dfs(i,mask):
            nonlocal m
            
            if mask == m:
                return 0
            
            if (i,mask) in dp:
                return dp[(i,mask)]
            if i == None:
                return float('inf')
            
            res = float('inf')
            for x in graph[i]:
                res = min(res, dfs(x, mask | (1 << x)) + 1)
            
            dp[(i,mask)] = res            
            return res
        
        res = float('inf')
        for i in range(len(graph)):
            res = min(res, dfs(i, 0 | (1 << i)))
        '''
        res = float('inf')
        
        for node in range(len(graph)):
            heap = [[0,node,0 | (1 << node)]]
            dp = {}
            while heap:

                cost, n, mask = heappop(heap)
                if mask == m:
                    res = min(res,cost)
                    break
                if (n,mask) in dp:
                    continue
                
                dp[(n,mask)] = True
                
                for val in graph[n]:
                    if (val, mask | (1 << val)) in dp:
                        continue
                    heappush(heap, [cost + 1, val, mask | (1 << val)])
        
        
        return res
