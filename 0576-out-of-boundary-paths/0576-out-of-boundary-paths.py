class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        def oob(i,j):
            if i < 0 or i >=m or j < 0 or j >= n:
                return 1
            else:
                return 0
            
        @cache
        def dfs(i,j, moves):
            
            if moves == 0:
                return oob(i,j)
            if oob(i,j):
                return 1
            
            res = 0
            for x,y in directions:
                res += dfs(i+x, j+y,moves-1)
                res %= MOD

            return res % MOD
        
        MOD = 10 ** 9 + 7
        return dfs(startRow, startColumn, maxMove) % MOD
            
            