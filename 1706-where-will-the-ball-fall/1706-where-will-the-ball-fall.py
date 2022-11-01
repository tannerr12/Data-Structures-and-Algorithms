class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        
        balls = [[(0,0) for j in range(len(grid[0]))] for i in range(len(grid) +1)]
        
        
        for c in range(len(balls[0])):
            balls[0][c] = (1, c)
        #print(balls)
        
        for i in range(len(grid)):
            for j in range(len(grid[i]) -1):
                l = grid[i][j]
                r = grid[i][j +1]

                
                
                if l == 1 and r == 1:

                    balls[i+1][j + 1] = balls[i][j]
                    
                        
                
                elif l == -1 and r == -1:
                    
                    balls[i+1][j] = balls[i][j+1]
                    
                
                
#elif l == -1 and r ==1

        
    
    
        #print(balls)
        res = [-1 for i in range(len(balls[-1]))]
        count = 0
        for x,y in balls[-1]:
            
            if x >= 1:
                res[y] = count
                
            count += 1
        
        return res
            
            
                
                
                