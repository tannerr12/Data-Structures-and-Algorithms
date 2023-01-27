class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])

        @cache
        def dfs(r,c,count):
            
            if r >= m or c >= n:
                return False
            
            if grid[r][c] == ')':
                count -=1
            else:
                count +=1
            
            if count < 0:
                return False
            
            if r == m-1 and c == n-1:
                
                return count == 0
            
            res = False    
            #go right
            res = res or dfs(r+1,c,count)
            #go down
            res = res or dfs(r,c+1,count)
            
            return res
        
        return dfs(0,0,0)
    
            
            
                