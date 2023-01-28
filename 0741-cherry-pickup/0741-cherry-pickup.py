class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n,m = len(grid), len(grid[0])
      
        
        @cache
        def dfs(r1,c1,c2):
            add = 0

            r2 = r1 + c1 - c2
            if r1 >= n or r2 >= n or c1 >= m or c2 >= m or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if r1 == r2 and c1 == c2 and grid[r1][c1] == 1:
                add +=1
            else:
                if grid[r1][c1] == 1:
                    add +=1
                if grid[r2][c2] == 1:
                    add +=1

            if r1 == len(grid) -1 and r2 == len(grid)-1 and c1 == len(grid[0]) -1 and c2 == len(grid)-1:
                return add
            

            res = float('-inf')
            
            #combinations of moves [down,right] [right,down], [down,down],[right,right]
            
            #down, right
            res = max(res,dfs(r1+1, c1, c2 +1) + add)
            
            #right down
            res = max(res,dfs(r1,c1+1,c2) + add)
            
            #down down
            res = max(res,dfs(r1 + 1, c1, c2) + add)
            
            #right, right
            res = max(res,dfs(r1, c1 + 1,c2 + 1) + add)
            
             
            return res
            
        
        
        res = dfs(0,0,0)
        
        return res if res != float('-inf') else 0