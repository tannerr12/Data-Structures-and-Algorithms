class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        
        #mat1 is the source
        res = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
        
        #print(res)
        
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                
                total = 0
                for k in range(len(mat1[0])):
                    total += mat1[i][k] * mat2[k][j]
                
                res[i][j] = total
                
        
        
        return res