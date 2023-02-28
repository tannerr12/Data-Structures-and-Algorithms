class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent = [i for i in range(n)]
        rank = [0] * n
        count = n
        
        print(len(edges))
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
        
        #score = {}
        for i in range(len(edges)):
            edges[i].append(i)
        edges = sorted(edges, key=lambda x: (x[2]))
        score = set()
        phsudo = set()
        weight = 0
        #no edges removed
        for a,b,c,d in edges:

            if union(a,b):
                weight += c

        parent = [i for i in range(n)]
        rank = [0] * n
        
        for i in range(len(edges)):

            w = 0
            for a,b,c,d in edges:
                if d == i:
                    continue
                if union(a,b):
                    #tempScore.add(d)
                    w +=c
            
            if w != weight:
                score.add(i)
            parent = [i for i in range(n)]
            rank = [0] * n
        
        count = n-1
        for i in range(len(edges)):
            if edges[i][3] in score:
                continue
            w = 0
            w += edges[i][2]
            union(edges[i][0],edges[i][1])
            
            for a,b,c,d in edges:
                if d == edges[i][3]:
                    continue
                if union(a,b):
                    w +=c
                    
            
            if w == weight and count == 0:
                phsudo.add(edges[i][3])
            
            count = n-1
            parent = [i for i in range(n)]
            rank = [0] * n
        
        #print(score)
        phsudo = phsudo - score
        res = list(score)
        res1  = list(phsudo)
            
        return [res,res1]