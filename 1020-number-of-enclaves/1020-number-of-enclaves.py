class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        parent = [i for i in range(m * n)]
        
        rank = [0] * (m*n)
        
        seen = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        @cache
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1 or (i,j) in seen:
                return
            
            seen.add((i,j))
            
            for x,y in directions:
                
                dfs(i+x,j+y)
        
        
        
        count = 0
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]:
                    count +=1
                    if i == 0 or j == 0 or i == m -1 or j == n -1:
                        dfs(i,j)
        
                
        return count - len(seen)
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
            
            
            return False

        """
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]:
                    
                    for x,y in directions:
                        newx,newy = x + i, y + j
                        if newx < 0 or newx >= m or newy < 0 or newy >= n or grid[newx][newy] != 1:
                            continue
                        
                        union((newx + 1) * newy, (i + 1) * j)
        """             
            
        print(parent)               