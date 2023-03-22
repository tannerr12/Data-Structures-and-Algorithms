class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * (n + 1)
        #print(parent)
        def find(val):
            
            if parent[val] == val:
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
                    parent[v2] = v1
                    rank[v1] +=1
        
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        for s, d, dist in roads:
            union(s-1,d-1)
        
        
        res = float('inf')
        for s, d, dist in roads:
            if isConnected(0, d-1):
                res = min(res,dist)
        
        return res
            
        
            