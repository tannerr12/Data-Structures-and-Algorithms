class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        grid = [[-1 for j in range(n)] for i in range(m)]
        
        moves = [[-2,-1], [-2,1], [-1,-2], [1,-2], [-1,2],[1,2],[2,1],[2,-1]]
        ans = []
        def dfs(x,y,depth):
            nonlocal ans

            if depth == m * n:
                #ans = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
                return True
            

            for a,b in moves:
                
                newx,newy = x + a, y + b
                
                if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] != -1:
                    continue
                
                grid[newx][newy] = depth
                if dfs(newx,newy,depth + 1): return True
                grid[newx][newy] = -1
        
        grid[r][c] = 0
        dfs(r,c,1)
        
        return grid