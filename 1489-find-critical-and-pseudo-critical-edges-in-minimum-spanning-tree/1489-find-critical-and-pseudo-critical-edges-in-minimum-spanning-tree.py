class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent = [i for i in range(n)]
        rank = [0] * n
        count = n-1
        
        #First we setup union find for MST than we sort the edges by weight and include its index in the array
        #next we do 2 cycles 
        #The first cycle will find all critical edges by checking if without that edge the weight of the tree increases
        #the second cycle will find all psudo edges by checking all edges and adding them by force than checking if the weight of the 
        #tree is still the optimal weight if not than it is not a psudo
        
        def find(val):
            
            if val == parent[val]:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x,y):
            nonlocal count
            v1,v2 = find(x),find(y)
            
            
            if v1 != v2:

                if rank[v1] > rank[v2]:    
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    parent[v2] = v1
                    rank[v1] +=1
                    
                count -=1
                return True
            
            return False
        
        
        
        #build out edges

        for i in range(len(edges)):
            edges[i].append(i)
        edges = sorted(edges, key=lambda x: (x[2]))
        crit = []
        pseudo = []
        weight = 0
        #no edges removed
        for a,b,c,d in edges:
            if union(a,b):
                weight += c
            if count == 0:
                break
        parent = [i for i in range(n)]
        rank = [0] * n
        count = n-1
        
        #check for crit
        for i in range(len(edges)):
            w = 0
            for a,b,c,d in edges:
                if d == i:
                    continue
                if union(a,b):
                    w +=c
                if count == 0:
                    break
                    
            if w != weight:
                crit.append(i)
                
            parent = [i for i in range(n)]
            rank = [0] * n
            count = n-1
        
        #check for pseudo
        for i in range(len(edges)):
            if edges[i][3] in crit:
                continue
         
            w = edges[i][2]
            union(edges[i][0],edges[i][1])
            
            for a,b,c,d in edges:
                if d == edges[i][3]:
                    continue
                if union(a,b):
                    w +=c
                
                if count == 0:
                    break
            
            if w == weight and count == 0:
                pseudo.append(edges[i][3])
            
            count = n-1
            parent = [i for i in range(n)]
            rank = [0] * n

        return [crit,pseudo]