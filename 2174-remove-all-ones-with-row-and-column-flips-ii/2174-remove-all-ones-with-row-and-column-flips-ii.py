class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        
        row,col = set(),set()
        
        #needr = set()
        #needc = set()
        marked = set()
        m,n = len(grid), len(grid[0])
        
        for i in range(m):
            
            for j in range(n):
                
                if grid[i][j] == 1:
                    marked.add((i,j))
                    row.add(i)
                    col.add(j)
                  
        
        
        def backtrack(r,c):
            
            if r == m:
                valid = True
                
                for x,y in marked:
                    if x not in row or y not in col:
                        continue
                    else:
                        valid = False
                        break
                        
                if valid:
                    return 0
                else:
                    return float('inf')
            
            res = float('inf')
            
            #get next value
            tr,tc = r,c
            tc += 1
            if tc == n:
                tc = 0
                tr +=1
            
            #take
            if grid[r][c] == 1 and (r in row and c in col):
                
                ar,ac = False,False
                if r in row:
                    row.remove(r)
                    ar = True
                if c in col:
                    col.remove(c)
                    ac = True
                marked.remove((r,c))
                res = min(res,backtrack(tr,tc) + 1)
                marked.add((r,c))
                if ar:
                    row.add(r)
                if ac:
                    col.add(c)

            #dont take
            
            res = min(res, backtrack(tr,tc))
            
            return res
        
        
        return backtrack(0,0)