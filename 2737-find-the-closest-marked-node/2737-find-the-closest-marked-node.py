class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        
        adj = defaultdict(list)
        mk = set(marked)
        for u,v,w in edges:
            adj[u].append([v,w])
        
        heap = [[0,s]]
        seen = set()
        
        while heap:
            
            weight,node = heappop(heap)
            
            if node in mk:
                return weight
            seen.add(node)
            for v,w in adj[node]:
                
                if v in seen:
                    continue
            
                heappush(heap, (weight + w, v))
                
            
        return -1