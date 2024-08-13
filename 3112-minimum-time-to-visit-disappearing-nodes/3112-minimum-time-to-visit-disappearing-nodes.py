class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        
        q = [(0,0)]
        ans = [-1] * n
        adj = defaultdict(list)
        
        for x,y,z in edges:
            adj[x].append((y,z))
            adj[y].append((x,z))
        
        
        seen = set()
        while q:
            
            cost,val = heappop(q)
            if val in seen:
                continue
            seen.add(val)
            if cost < disappear[val]:
                ans[val] = cost
            else:
                continue
                
            for v,c in adj[val]:
                
                heappush(q, (c + cost, v))
                    
                    
        
        return ans