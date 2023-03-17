class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        prefixMpI = defaultdict(list)
        prefixMpJ = defaultdict(list)
        for i in range(m):
            prefixMpI[i].append(0)
            for j in range(n):
                
                prefixMpI[i].append(grid[i][j] + prefixMpI[i][-1])
                if j not in prefixMpJ:
                    prefixMpJ[j].append(0)
                    
                prefixMpJ[j].append(grid[i][j] + prefixMpJ[j][-1])
        
        
        #print(prefixMpI)
        #print(prefixMpJ)
        
        res = 0
        for i in range(m -2):
            for j in range(n -2):
                total = -1
                valid = True
                #check 3 right
                for x in range(3):
                    a = i + 2
                    b = j + x
                    newtotal = prefixMpJ[b][a+1] - prefixMpJ[b][i] 
                
                    if total == -1:
                        total = newtotal
                    elif total != newtotal:
                        valid = False
                    
                    
                    
                #check 3 down
                for x in range(3):
                    a = i + x
                    b = j + 2
                    newtotal = prefixMpI[a][b+1] - prefixMpI[a][j] 
                
                    if total == -1:
                        total = newtotal
                    elif total != newtotal:
                        valid = False
                    
                t = 0
                #check diag down
                for x in range(3):
                    
                    t += grid[i+x][j+x]
                
                if t != total:
                    valid = False
            
                    
                t = 0
                #check diag up
                for x in range(3):
                    
                    t += grid[i+2-x][j+x]
                
                seen = set()
                
                for ii in range(3):
                    for jj in range(3):
                        if grid[ii + i][jj + j] > 9 or grid[ii + i][jj + j] == 0:
                            valid = False
                            break
                        seen.add(grid[ii + i][jj + j])
                
                
                if t != total:
                    valid = False
                if valid and len(seen) == 9:
                    res +=1
                
                
                    
        return res