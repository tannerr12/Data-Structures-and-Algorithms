class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        parent = [i for i in range(n)]
        rank = [0]  * n
        res = 0
        count = n
        def find(val):
            
            if val == parent[val]:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
        
        def union(x,y,time):
            nonlocal res
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
                
                res = max(res,time)
                count -=1
                
        def isConnected(x,y):
            return find(x) == find(y)
        
        
        for t,x,y in logs:
            union(x,y,t)
        
    
        
        return res if count == 1 else -1
        