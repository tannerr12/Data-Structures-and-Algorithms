class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        res = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]

        for i in range(len(mat1)):
            for k in range(len(mat1[0])):
                # Skip calculation if the mat1 element is zero
                if mat1[i][k] == 0:
                    continue

                for j in range(len(mat2[0])):
                    # Skip calculation if the mat2 element is zero
                    if mat2[k][j] == 0:
                        continue

                    res[i][j] += mat1[i][k] * mat2[k][j]

        return res






