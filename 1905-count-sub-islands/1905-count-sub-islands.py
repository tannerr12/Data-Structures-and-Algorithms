class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n,m = len(grid1), len(grid1[0])

        memo = set()
        def dfs(r,c):

            if r == n or r < 0 or c == m or c < 0 or grid2[r][c] == 0 or (r,c) in memo:
                return True

            memo.add((r,c))
            res = True
            if grid1[r][c] ==0:
                res= False
            
            
            #check 4 directions
            res = dfs(r+1, c) and res
            res = dfs(r-1, c) and res 
            res = dfs(r, c+1) and res 
            res = dfs(r,c-1) and res 

            return res
            
        
        result = 0
        for r in range(n):
            for c in range(m):
                if grid2[r][c] == 1 and (r,c) not in memo:
                    if dfs(r,c):
                        result +=1
                   

        return result
            


