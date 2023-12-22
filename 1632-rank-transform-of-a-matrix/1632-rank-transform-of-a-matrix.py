
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        
        
        def find(x):
            
            if x != parent[x]:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x,y):
            
            x1 = find(x)
            y1 = find(y)
            
            if x1 != y1:
                parent[x1] = y1
            
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        
        
        rankX = [0] * m
        rankY = [0] * n
        
        mp = defaultdict(list)
        for i in range(m):
            for j in range(n):
                mp[matrix[i][j]].append([i,j])
            
        
        grid = [[0 for j in range(n)] for i in range(m)]
        for val in sorted(mp):
            
            parent = list(range(m+n))
            
            for i,j in mp[val]:
                union(i, j+m)
            
            root = defaultdict(int)
            for i,j in mp[val]:
                r = find(i)
                root[r] = max(root[r], max(rankX[i], rankY[j]) + 1)
            
            for i,j in mp[val]:
                r = find(i)
                ra = root[r]
                grid[i][j] = ra
                rankX[i] = ra
                rankY[j] = ra
                
        
        return grid
                
            