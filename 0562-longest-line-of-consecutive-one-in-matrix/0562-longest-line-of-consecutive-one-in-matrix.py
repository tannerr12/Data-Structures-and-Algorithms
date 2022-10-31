class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        
        n,m = len(mat), len(mat[0])
        row = collections.defaultdict(int)
        col = collections.defaultdict(int)
        
        upDiag = collections.defaultdict(int)
        dwDiag = collections.defaultdict(int)
        
        
        
        
        #def checklen(r,c):
            
         #   if r >= n or r < 0 or c >= m or c < 0:
          #      return 0
            
            
            
        res = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                
                if mat[r][c] == 1:
                    row[r] +=1
                    col[c] +=1
                    dwDiag[r-c] +=1
                    upDiag[r+c] +=1
                    res = max(row[r], col[c], dwDiag[r-c], upDiag[r+c], res)
                else:
                    row[r] = 0
                    col[c] = 0
                    dwDiag[r-c] = 0
                    upDiag[r+c] = 0
                    
        
        

            
        return res
                        
        
  
                        
                
        