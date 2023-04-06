class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m-2):
            for j in range(n-2):
                
                #calculate hourglass
                top = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                mid = grid[i+1][j+1]
                bot = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                
                res = max(res, top + mid + bot)
                
        
        return res
                
                
                
        