class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        
        for x,y,z in edges:
            
            adj[x].append([y,z])
            adj[y].append([x,z])
        
        short = [float('inf')] * n
        
        
        s = set()
        heap = [[0, n]]
      
        
        
        while heap:
            
            cost,node = heappop(heap)
           
            if node in s:
                continue
            s.add(node)
            short[node-1] = min(short[node-1], cost)
            
            for nod,c in adj[node]:
                
                if nod in s:
                    continue
           
                heappush(heap,[cost + c, nod])
        
        
        #print(short)
        
        MOD = 10 ** 9 + 7
        seen = set()
        seen.add(1)
        
        @cache
        def dfs(node):
            
            if node == n:
                return 1
            
            total = 0
            for x,c in adj[node]:
                
                if short[x-1] >= short[node-1]:
                    continue
                
                total += dfs(x)
                total %= MOD
            
            
            return total
        
        return dfs(1) % MOD
                
                
                
            
            
            
        