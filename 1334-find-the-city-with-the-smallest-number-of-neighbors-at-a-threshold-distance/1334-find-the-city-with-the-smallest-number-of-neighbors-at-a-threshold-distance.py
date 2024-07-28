class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        #bfs each node to track the distance and subtract threshold as you go


        adj = [[float('inf') for i in range(n)] for j in range(n)]

        

        
        for x,y,z in edges:

            adj[x][y] = z
            adj[y][x] = z
            adj[x][x] = 0
            adj[y][y] = 0

        print(adj)



        def floya(count,dist):

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        adj[i][j] = min(adj[i][j], adj[k][j] + adj[i][k])
        

        floya(n,adj)
        minNodeCount = n
        minNode = -1

        for i in range(n):
            curr = 0
            for j in range(n):
                if i==j:
                    continue
                if adj[i][j] <= distanceThreshold:
                    curr+=1
            
            if minNodeCount >= curr:
                minNodeCount = curr
                minNode = i
        

        return minNode