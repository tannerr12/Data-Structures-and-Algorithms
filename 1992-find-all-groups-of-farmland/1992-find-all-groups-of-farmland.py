class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        def check(i,j):
            
            if i < 0 or j < 0 or land[i][j] == 0:
                return False
            return True
        
        def getVal(i,j):
            
            if i < 0 or j < 0:
                return 0
            
            return land[i][j]
        
        groups = []
        gcount = 1
        for i in range(len(land)):
            for j in range(len(land[0])):
                
                if land[i][j] == 0:
                    continue
                up = check(i-1,j)
                left = check(i,j-1)
                
                #start block
                if not up and not left:
                    groups.append([i,j,i,j])
                    land[i][j] = gcount
                    gcount += 1
                    
                elif up or left:
                    land[i][j] = max(getVal(i-1,j), getVal(i,j-1))
                    groups[land[i][j]-1][2] = max(groups[land[i][j]-1][2],i)
                    groups[land[i][j]-1][3] = max(groups[land[i][j]-1][3],j)
        
      
        return groups
                    
                
                
                