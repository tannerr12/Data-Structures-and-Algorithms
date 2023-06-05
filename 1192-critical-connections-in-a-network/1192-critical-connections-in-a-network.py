class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        
        adj = defaultdict(list)
        rank = {}
        conn = {}
        
        for i in range(n):
            rank[i] = None
        
        for x,y in connections:
            
            adj[x].append(y)
            adj[y].append(x)
            conn[(min(x,y), max(x,y))] = 1
            
        
        def dfs(node,rankk):
            
            if rank[node]:
                return rank[node]
            
            rank[node] = rankk
            
            min_rank = rankk + 1
            
            for neigh in adj[node]:
                #dont check prev
                if rank[neigh] and rank[neigh] == rankk -1:
                    continue
                
                rec_rank = dfs(neigh, rankk + 1)
                
                if rec_rank <= rankk:
                    del conn[(min(node,neigh), max(node,neigh))]
                
                min_rank = min(min_rank, rec_rank)
            
            return min_rank
         
        
        dfs(0,0)
        res = []
        for u,v in conn:
            res.append([u,v])
        return res