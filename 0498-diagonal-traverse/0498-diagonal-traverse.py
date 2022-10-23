class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        
        res = []
        hx,hy = 0 ,0
        x,y = 0,0
        down = True
        count = 1
        firstHalf = True
        temp = []
        while len(res) != len(mat) * len(mat[0]):
            
            
            temp.append(mat[x][y])
            
            if not down:
                x -=1
                y +=1
            else:
                x+=1
                y-=1
            
            
            if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]):
                
                if count %2 == 0:
                    res.extend(temp)
                else:
                    res.extend(temp[::-1])
                    
                temp = []
                if hy +1 >= len(mat[0]):
                    y = hy
                    hx +=1
                    x = hx
                else:
                    hy +=1
                    y = hy
                    x = hx
     
                count +=1
        
                
                   
            
        return res