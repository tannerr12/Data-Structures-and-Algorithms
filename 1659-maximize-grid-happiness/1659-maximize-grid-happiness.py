class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def getHappiness(j,type, lastNValues):
            up = lastNValues[j]
            left = lastNValues[j-1] if j > 0 else ""
            
            up_diff = 0
            
            if up == "i":
                up_diff = -30
            
            elif up == "e":
                up_diff = 20
              
            left_diff = 0
            if left == "i":
                left_diff = -30
            
            elif left == "e":
                left_diff = 20
            
            neighbours = (1 if up else 0) + (1 if left else 0)
            
            ans = 0
            if type == 'i':
                ans = 120 - 30 * neighbours + left_diff + up_diff
            elif type == 'e':
                ans = 40 + 20 * neighbours + left_diff + up_diff
            
            return ans
        @cache
        def dp(pos,intro,extro, lastValues):
            if pos == m * n:
                return 0
            
            j = pos % n
            
            ans = 0
            lastValues_new = list(lastValues)
            oldVal = lastValues_new[j]
            #not place
            lastValues_new[j] = ""
            ans = max(ans, dp(pos + 1, intro, extro, tuple(lastValues_new)))
            lastValues_new[j] = oldVal
            #place intro
            if intro:
                happiness = getHappiness(j,"i",lastValues)
                lastValues_new[j] = "i"
                ans = max(ans, dp(pos + 1, intro-1, extro, tuple(lastValues_new)) + happiness)
                lastValues_new[j] = oldVal
            
            #place extro
            if extro:
                happiness = getHappiness(j,"e",lastValues)
                lastValues_new[j] = "e"
                ans = max(ans, dp(pos + 1, intro, extro-1, tuple(lastValues_new)) + happiness)
                lastValues_new[j] = oldVal
            
            
            return ans
        
        return dp(0, introvertsCount,extrovertsCount, tuple([""] * n))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        '''
        grid = [[0 for j in range(n)] for i in range(m)]
        
        directions = [[-1,0], [0, -1]]
        
        def calc(s,i,j):
            score = 0
            for x,y in directions:
                nx,ny = i + x, j + y
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                    if s == 2 and grid[nx][ny] == 2:
                        score -= 60
                    elif s == 1 and grid[nx][ny] == 1:
                        score += 40
                    elif s == 2 and grid[nx][ny] == 1:
                        score -= 10
                    elif s == 1 and grid[nx][ny] == 2:
                        score -= 10
            
            return score
                
                
        
        def checkGrid(grid):
            score = 0

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        score += 40 + calc(grid[i][j], i,j)
                    elif grid[i][j] == 2:
                        score += 120 + calc(grid[i][j], i,j)
            
        
            return score
        
        seen = {}
        
        
        def populate(i,ic,ec,last):
            
            if i == m or (ic == 0 and ec == 0):
                return 0
            
            res = float('-inf')
            #pos =  (i * n) + j
            #skip the current cell
            if j == n -1:
                res = max(res,populate(i+1,0,ic,ec))
                if ec:
                    grid[i][j] = 1
                    res = max(res,populate(i+1,0,ic,ec-1) + 40 + calc(grid[i][j], i,j))
                if ic:
                    grid[i][j] = 2
                    res = max(res, populate(i+1, 0, ic-1, ec) + 120 + calc(grid[i][j], i, j))
                grid[i][j] = 0
            else:
                res = max(res,populate(i,j+1,ic,ec))
                if ec:
                    grid[i][j] = 1
                    res = max(res,populate(i,j+1,ic,ec-1) + 40 + calc(grid[i][j], i,j))
                if ic:
                    grid[i][j] = 2
                    res = max(res, populate(i, j+1, ic-1, ec) + 120 + calc(grid[i][j], i,j))
                grid[i][j] = 0
            
        
            return res
            
        
        return populate(0,introvertsCount,extrovertsCount, tuple([0] * n))
        
            
        ''' 
            
                    