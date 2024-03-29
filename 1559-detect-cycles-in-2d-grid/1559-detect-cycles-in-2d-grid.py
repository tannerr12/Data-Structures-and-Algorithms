class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        n,m = len(grid), len(grid[0])
        
        seen = set()
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        
        
        def dfs(i,j,par,char):
            nonlocal n,m
            if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] != char:
                return False
            
            if (i,j) in seen:
                return True
            
            seen.add((i,j))
            res = False
            for x,y in directions:
                if (x + i, y + j) == par:
                    continue
                res = res or dfs(i+x, j+y, (i,j),char)
                
            
            return res
            
        
        for i in range(n):
            for j in range(m):
                if not (i,j) in seen:
                    if dfs(i,j,(-1,-1),grid[i][j]):
                        return True
        
        
        return False
        """ 
        n,m = len(grid), len(grid[0])  

        parent= {}
        rank = defaultdict(int)
        
        def find(val):
            
            if parent[val] == val:
                return val
            
            parent[val] = find(parent[val])
            return parent[val]
            
        def union(x,y):
            
            v1,v2 = find(x), find(y)
            
            
            if v1 != v2:
                
                if rank[v1] > rank[v2]:
                    parent[v2] = v1
                elif rank[v2] > rank[v1]:
                    parent[v1] = v2
                    
                else:
                    parent[v2] = v1
                    rank[v1] += 1
                
                return False
            
            return True
        
        def isConnected(x,y):
            return find(x) == find(y)
        
        
        for i in range(n):
            for j in range(m):
                
                if i + 1 < n and grid[i+1][j] == grid[i][j]:
                    if (i,j) not in parent:
                        parent[(i,j)] = (i,j)
                    if (i+1, j) not in parent:
                        parent[(i+1,j)] = (i+1,j)
                    if union((i,j), (i+1,j)):
                        return True
                
                if j + 1 < m and grid[i][j+1] == grid[i][j]:
                    if (i,j) not in parent:
                        parent[(i,j)] = (i,j)
                    if (i, j + 1) not in parent:
                        parent[(i,j+1)] = (i,j+1)
                    if union((i,j), (i,j+1)):
                        return True
        
        return False
                