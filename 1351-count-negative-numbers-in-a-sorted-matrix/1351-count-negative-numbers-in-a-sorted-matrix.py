class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        res = 0
        
        for i in range(len(grid)):
            l,r = 0, len(grid[0]) -1

            if grid[i][l] < 0 and grid[i][r] < 0:
                res += len(grid[i])
                continue
            while l <= r:


                curr  = (l+r) // 2



                if grid[i][curr] < 0 and grid[i][curr -1] >= 0:
                    res += len(grid[i]) - curr
                    break
                
                
                elif grid[i][curr] >= 0:
                    l = curr +1
                    
                
                else:
                    r = curr - 1
        
        
        return res
