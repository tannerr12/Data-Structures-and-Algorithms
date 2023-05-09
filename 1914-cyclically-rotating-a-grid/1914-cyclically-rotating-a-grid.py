class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        res = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        

        
        count = len(grid[0]) * len(grid)
        x,y = len(grid[0]),len(grid)
        subtractions = -1
        while count:
            

            borderSize = (y*2) + ((x-2) * 2)
            actualRotations = k % borderSize
            
            gather = []
            x -=1
            y -=1
            subtractions +=1
            a,b = y,x

            
            while a > subtractions:
                a-=1
                gather.append(grid[a][b])
            
            while b > subtractions:
                b-=1
                gather.append(grid[a][b])
            

            while a != y:
                a += 1
                gather.append(grid[a][b])
            
            while b != x:
                b+=1
                gather.append(grid[a][b])
            
            
            #print(gather)
            
            start = (-k) % len(gather)
            count -= len(gather)
            a,b = y,x

            
            while a > subtractions:
                a-=1
                res[a][b] = gather[start]
                start +=1 
                start %= len(gather)
            
            
            while b > subtractions:
                b-=1
                res[a][b] = gather[start]
                start +=1 
                start %= len(gather)
            
            
            while a != y:
                a += 1
                res[a][b] = gather[start]
                start +=1 
                start %= len(gather)
            
            
            while b != x:
                b+=1
                res[a][b] = gather[start]
                start +=1 
                start %= len(gather)
        
        return res
            

            
            
            
            