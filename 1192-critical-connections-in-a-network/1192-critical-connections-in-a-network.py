class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        
        adj = defaultdict(list)
        rank = {}
        conn = {}
        
        #create an array for rank
        for i in range(n):
            rank[i] = None
        
        #add edges once and build adj list
        for x,y in connections:
            
            adj[x].append(y)
            adj[y].append(x)
            conn[(min(x,y), max(x,y))] = 1
            
        
        def dfs(node,rankk):
            #if we have seen this node return its rank
            if rank[node]:
                return rank[node]
            
            #new node give it a rank prev + 1
            rank[node] = rankk
            
            #this is the expected next rank
            min_rank = rankk + 1
            
            for neigh in adj[node]:
                #dont check prev/skip parent
                if rank[neigh] and rank[neigh] == rankk -1:
                    continue
                #check neighbour with rank + 1
                rec_rank = dfs(neigh, rankk + 1)
                
                #the returned result is less or equal to our current rank so we found a cycle
                #delete the connection
                if rec_rank <= rankk:
                    del conn[(min(node,neigh), max(node,neigh))]
                #log our smallest rank seen
                min_rank = min(min_rank, rec_rank)
            
            #pass up our lowest rank seen
            return min_rank
         
        
        dfs(0,0)
        res = []
        #add the non cycle connections to res and return 
        for u,v in conn:
            res.append([u,v])
        return res