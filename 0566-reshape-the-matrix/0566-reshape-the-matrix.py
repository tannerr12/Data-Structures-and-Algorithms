class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        if r * c != len(mat) * len(mat[0]):
            return mat
        tres = []
        res = []
        

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                 tres.append(mat[i][j])
                    
       
    
        for i in range(0,len(tres), c):
            res.append(tres[i:i+c])
        
        return res
            