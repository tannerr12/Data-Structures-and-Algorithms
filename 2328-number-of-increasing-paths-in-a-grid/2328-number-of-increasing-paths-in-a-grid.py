class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        directions = [[-1,0], [1, 0], [0,-1], [0,1]]
        dp = {}
        
        def dfs(i, j):
            
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            
            res  = 0 
            for x,y in directions:
                newx,newy = i + x, j + y
                if newx < 0 or newy < 0 or newx >= len(grid) or newy >= len(grid[0]) or grid[newx][newy] <= grid[i][j]:
                    continue
                    
                res += dfs(newx,newy) + 1
                res %= MOD
                    
            dp[(i,j)] = res
            return res % MOD
        
        MOD = 10 ** 9 + 7
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(i,j) % MOD 
        
        return (res + (len(grid) * len(grid[0]))) % MOD
            