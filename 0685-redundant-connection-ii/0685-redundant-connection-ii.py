class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        rank = [1] * (len(edges)+1)
        par = [i for i in range(len(edges) +1)]

        
        def find(p):
            
            if par[p] == p:
                return p
            
            par[p] = find(par[p])
            
            return par[p]
        
        
        def union(n1,n2):
            
            p1,p2 = find(n1), find(n2)
            
            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                
       
            elif rank[p2] > rank[p1]:
                par[p1] = p2
            
            else:
                par[p2] = p1
                rank[p1] += 1
            

            return False
        
        
        count = defaultdict(int)
        parent = defaultdict(int)
        bad = None
        for x,y in edges:
            count[y] +=1
            parent[x] +=1
            if count[y] == 2:
                bad = y
                
        
        
        if not bad:    
            for x,y in edges:
                if union(x,y):
                    return [x,y]
            
        connections = set()
        for x,y in edges:
            if x == bad:
                connections.add((y,x))
        for x,y in edges:
            
            if y == bad:
                if (x,y) in connections:
                    return [x,y]
                
                if parent[x] > 1 or count[x] > 0:
                    ans = [x,y]
    
        return ans
        
        