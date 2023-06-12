class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        #can never pass 3
        #5! = 120 possible combinations
        #only 2 and 4 matter
        
        #edge case
        if len(grid) == 1:
            for j in range(len(grid[0])):
                if grid[0][j] == 1:
                    return []
            return [0]
        
        res = []
        row = {}
        for i in range(len(grid)):
            mask = 0
            for j in range(len(grid[0])):
                if grid[i][j]:
                    mask |= (1 << j)
             
            row[i] = mask
            
                
        for i in range(len(list(row))):
            for j in range(i + 1, len(list(row))):
                if row[i] & row[j] == 0:
                    return [i,j]
                
        return []
     
        