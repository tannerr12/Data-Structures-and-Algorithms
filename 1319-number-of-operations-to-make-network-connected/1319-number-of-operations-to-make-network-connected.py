class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #Check how many groups we have -1
        #this will guarentee us enough cables
        if len(connections) < n - 1:
            return -1
        
        parent = [i for i in range(n)]
        rank = [0] * n
        
        
        def find(val):
            
            if val == parent[val]:
                
                return val
            
            parent[val] = find(parent[val])
            
            return parent[val]
        
        
        def union(x,y):
            
            v1,v2 = find(x),find(y)
            
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    rank[v1] +=1
                    parent[v2] = v1
        
        unique = set()
        for x,y in connections:    
            union(x,y)
        
        for i in range(len(parent)):
            unique.add(find(i))
        
        
        return len(unique) -1
        