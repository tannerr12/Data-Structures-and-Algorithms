class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        
        
        adj = defaultdict(list) 
        
        for x,y,z in connections:
            adj[x].append((y,z))
            adj[y].append((x,z))
            
        
        
        
        
        heap = []
        heap.append((0, 1))
        
        
        seen = set()
        res = 0
        dp = [0] * (n +1)
        while heap:
            
            cost,val = heapq.heappop(heap)
            
            if val in seen:
                continue
            
            seen.add(val)
            
            dp[val] = cost
            if len(seen) == n:
              #  print(dp)
                return sum(dp)
            
            for node,dist in adj[val]:
                heappush(heap,(dist, node))
                
        
        
        
        
        
        return -1
                