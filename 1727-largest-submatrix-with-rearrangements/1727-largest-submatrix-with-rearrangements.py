class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        #find the longest column sequence length than sort each row by 
        #the sequence length and multiply its value by its sorted position in the grid
        #this is possible if we sort in decreasing order since we can assume previous
        #columns are valid to use
        for j in range(len(matrix[0])):
            for i in range(len(matrix) -2, -1,-1):
                if matrix[i][j] > 0:
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j]
            
        
        res = 0
        for i in range(len(matrix)):
            matrix[i].sort(reverse = True)
            for j in range(len(matrix[0])):

                res = max(res,matrix[i][j] * (j + 1))
        
        return res
                