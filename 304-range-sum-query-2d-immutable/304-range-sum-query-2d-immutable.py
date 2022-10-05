class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix
        self.dp = collections.defaultdict(int)
        
        for i in range(len(matrix)):
            s=0
            for j in range(len(matrix[0])):
                above = self.dp[(i-1, j)]
                s += matrix[i][j]
                self.dp[(i,j)] = s + above
                
        
        #print(self.dp)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            
            above = self.dp[(row1-1,col2)]
            left = self.dp[(row2, col1-1)]
            
            return (((self.dp[(row2,col2)] - above) - left) + self.dp[(row1-1,col1-1)])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)