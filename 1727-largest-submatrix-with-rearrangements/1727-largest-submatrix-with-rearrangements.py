class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        
        for j in range(len(matrix[0])):
            for i in range(len(matrix) -2, -1,-1):
                if matrix[i][j] > 0:
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j]
            
        
        #print(matrix)
        res = 0
        for i in range(len(matrix)):
            matrix[i].sort(reverse = True)
            for j in range(len(matrix[0])):

                res = max(res,matrix[i][j] * (j + 1))
        
        return res
                