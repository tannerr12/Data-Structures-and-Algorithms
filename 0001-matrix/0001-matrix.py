class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = []
        for i in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[i][x] == 0:
                    q.append([i,x])
                else:
                    mat[i][x] = "#"
        
        
         
        direction = [[-1,0],[1,0],[0,-1], [0,1]]
        
        for row,column in q:
            for dx,dy in direction:
                nr = row + dx
                nc = column + dy
                
                if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]) and mat[nr][nc] == "#":
                
                    mat[nr][nc] = mat[row][column] +1
                    q.append([nr,nc])
                    
        
        return mat
                
            
        
        