class Solution:
    def totalNQueens(self, n: int) -> int:
        
   
        diagr = set()
        diagc = set()
        row = set()
        col = set()
        
        
        
        def backtrack(r,c, num):
          
            if r >= n or num == 0:
                if num != 0:
                    return 0
                else:
              
                    return 1
            
            m = 0
            if r - c not in diagr and r + c not in diagc and r not in row and c not in col:
                diagr.add(r-c)
                diagc.add(r+c)
                row.add(r)
                col.add(c)
                tempC = c
                tempR = r
                if c + 1 >= n:
                    tempC = -1
                    tempR +=1
                
                m += backtrack(tempR, tempC+1, num -1)
               
             
                diagr.remove(r-c)
                diagc.remove(r+c)
                row.remove(r)
                col.remove(c)
           
            if c + 1 >= n:
                c = -1
                r +=1
            m += backtrack(r, c+1, num)
                
            return m
        return backtrack(0,0,n)    
