class Solution:
    def totalNQueens(self, n: int) -> int:
        
        res = 0
        diagr = set()
        diagc = set()
        row = set()
        col = set()
        #result = []
        
        #@cache
        def backtrack(r,c, num):
            nonlocal res
            if r >= n or num == 0:
                if num != 0:
                    return 0
                else:
                    #res +=1
                    #result.append(tempres.copy())
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
                #tempres.append((r,c))
                m += backtrack(tempR, tempC+1, num -1)
               
                #tempres.pop()
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
       # print(result)
        #return res