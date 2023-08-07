# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        parent = [i for i in range(n)]
    
        rank = [0] * n
            
        
        def find(x):
            
            if x == parent[x]:
                return x
            
            parent[x] = find(parent[x])
            
            return parent[x]
            
        
        def Union(x,y):
            
            v1,v2 = find(x), find(y)
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                else:
                    parent[v2] = v1
                    rank[v1] += 1
                
            
        for i in range(n):
            
            for j in range(i+1, n):
                
                if categoryHandler.haveSameCategory(i,j):
                    Union(i,j)
        
        
        #print(parent)
        
        
        return len(set(parent))