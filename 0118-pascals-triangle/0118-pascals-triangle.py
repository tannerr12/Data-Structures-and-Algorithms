class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        
        for i in range(1,numRows):
            temp = [1]
            
            for j in range(i-1):
                temp.append(arr[-1][j] + arr[-1][j+1])
        
            
            temp.append(1)
            arr.append(temp)
        
        return arr