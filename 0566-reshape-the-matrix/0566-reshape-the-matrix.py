class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        if r * c != len(mat) * len(mat[0]):
            return mat
        tres = []
        res = []
        
        tc = c 
        tr = r
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                 tres.append(mat[i][j])
                    
        
        temp = []
        for i in range(len(tres)):
            temp.append(tres[i])
            
            tc -=1
            
            if tc <= 0:
                res.append(temp.copy())
                temp = []
                tc = c
                tr -=1
        
        return res if len(res) > 0 and (r > 1 or c > 1) else [tres]
            