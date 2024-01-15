class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        grid = [[0 for j in range(n)] for i in range(n)]
        
        dig.sort()
        idx = 0
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
               
                if idx < len(dig) and [i,j] == dig[idx]:
                    idx +=1
                    grid[i][j] = 1
        
        #print(grid)
        
        res = 0
        for i in range(len(artifacts)):
            
            r1,c1,r2,c2 = artifacts[i]
            
            found = True
            for j in range(r1, r2 + 1):
                
                for k in range(c1, c2 + 1):
                    
                    if grid[j][k] != 1:
                        found = False
                        break
                
                if not found:
                    break
            
            if found:
                res += 1
        
        return res