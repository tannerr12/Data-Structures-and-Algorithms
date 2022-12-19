class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        parent = [i for i in range(n)]

        def find(index):

            if index != parent[index]:
                parent[index]= find(parent[index])

            
            return parent[index]

        
        def union(x,y):

            x1,y1  = find(x), find(y)

            if x1 != y1:
                    parent[x1] = y1
            

        

        for x,y in edges:
            union(x,y)

        
        #print(parent)
        return find(source) == find(destination)

