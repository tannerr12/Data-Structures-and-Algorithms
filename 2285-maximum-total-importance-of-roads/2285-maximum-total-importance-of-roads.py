class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
    
    
        adj = defaultdict(list)
        heap = []
        for x,y in roads:
            
            adj[x].append(y)
            adj[y].append(x)
            
        
        
        for key,val in adj.items():
            
            heappush(heap,(-len(val), key))

        
        
        cost = defaultdict(int)
        c = n
        while heap:
            v,d = heappop(heap)
            cost[d] = c
            c-=1
        
    
        res = 0
        for x,y in roads:
            res += cost[x] + cost[y]
            
        
        
        return res
            
        