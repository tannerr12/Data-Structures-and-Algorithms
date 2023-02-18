class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        
        for x,y in roads:
            
            adj[x].add(y)
            adj[y].add(x)
            
        
        
        res = 0
        
        for i in range(n):
            for j in range(i+1, n):
                total = len(adj[i]) + len(adj[j])
                if i in adj[j]:
                    total -=1
                res = max(res,total)
                
        
        return res