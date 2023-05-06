class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        
        m, n = len(matrix), len(matrix[0])
        
        '''
        for i in range(m):
            for j in range(n):
                right,down,curr = 0,0,matrix[i][j]
                if i < m-1:
                    down = matrix[i+1][j]
                if j < n-1:
                    right = matrix[i][j+1]
                
                
                option = 1
                #try leaving it
                total = curr + down + right
                
                #try #swaping right
                if right and (curr * -1) + down + (right * -1) > total:
                    total = (curr * -1) + down + (right * -1)
                    option = 2
                
                #try swapping down
                if down and (curr * -1) + (down * -1) + right > total:
                    total = (curr * -1) + (down * -1) + right
                    option = 3
                
                #try swapping right than down
                if right and down and curr + (down * -1) + (right * -1) > total:
                    total = curr + (down * -1) + (right*-1)
                    option = 4
              
            
                
                if option == 2:
                    if right != 0:
                        matrix[i][j+1] *= -1
                    matrix[i][j] *= -1
                elif option == 3:
                    if down != 0:
                        matrix[i+1][j] *= -1
                    matrix[i][j] *=-1
                elif option == 4:
                    if down != 0:
                        matrix[i+1][j] *= -1
                    if right != 0:
                        matrix[i][j+1] *= -1
                    
        
        
        '''
        mn = float('inf')
        negCount = 0

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] < 0:
                    negCount += 1
                mn = min(abs(matrix[i][j]), mn)
                res += abs(matrix[i][j])
                
        if negCount % 2 == 0:
            return res
        else:
            return res - (mn * 2)