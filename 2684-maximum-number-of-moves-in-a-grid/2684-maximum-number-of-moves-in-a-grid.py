class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [[-1,1], [0,1], [1,1]]
        memo = defaultdict(int)
        
        def dfs(i,j):
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            for x,y in directions:
                if i+x >= m or i+x < 0 or j+y >= n or j+y < 0:
                    continue
                if grid[i+x][j+y] > grid[i][j]:
                    res = max(res,dfs(i+x,j+y) + 1)
            
            memo[(i,j)] = res
            return res
        
        res = 0
        for j in range(len(grid)):
            
            res = max(res, dfs(j, 0))
        
        return res