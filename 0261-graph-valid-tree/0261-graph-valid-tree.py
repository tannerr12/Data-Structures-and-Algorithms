class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
            if len(edges) > n-1:
                return False
            parent = [i for i in range(n)]
            rank = [1] * n
            count = n
            def find(val):
                
                if val == parent[val]:
                    return val
                    
                parent[val] = find(parent[val])
                return parent[val]
            
            def union(x,y):
                nonlocal count
                v1 = find(x)
                v2 = find(y)
                
                if v1 != v2:
                    
                    if rank[v1] > rank[v2]:
                        parent[v2] = v1
                    elif rank[v2] > rank[v1]:
                        parent[v1] = v2
                    else:
                        parent[v2] = v1
                        rank[v1] +=1
                    count -=1
            def isConnected(x,y):
                return find(x) == find(y)
            
            for x,y in edges:
                union(x,y)
            
            
            #print(parent)
            
            return count == 1
                