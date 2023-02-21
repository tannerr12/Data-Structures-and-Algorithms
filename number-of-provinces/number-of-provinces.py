class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        parent = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)
        
        
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            
            return parent[val]
        
        def union(x,y):
            
            val1 = find(x)
            val2 = find(y)
            
            if val1 != val2:
                
                #they are not the same
                if rank[val1] > rank[val2]:
                    parent[val2] = val1
                elif rank[val2] > rank[val1]:
                    parent[val1] = val2
                
                else:
                    parent[val2] = val1
                    rank[val1] +=1
            
        
        def Connected(x,y):
            return find(x) == find(y)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(i,j)
        
        for i in range(len(isConnected)):
            find(i)
        #print(parent)
        
        return len(set(parent))