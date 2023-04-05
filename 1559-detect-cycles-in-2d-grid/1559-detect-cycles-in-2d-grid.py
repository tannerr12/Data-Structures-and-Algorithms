class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
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
            
            
            