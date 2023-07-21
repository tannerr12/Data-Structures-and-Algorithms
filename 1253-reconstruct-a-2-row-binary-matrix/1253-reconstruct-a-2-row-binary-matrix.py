class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        
        
        grid = [[0 for j in range(len(colsum))] for i in range(2)]
        

        for i in range(len(colsum)):
            
            if colsum[i] == 2:
                upper -= 1
                lower -= 1
                grid[0][i] = 1
                grid[1][i] = 1
            
            elif colsum[i] == 1:
                if upper >= lower:
                    upper -=1
                    grid[0][i] = 1
                else:
                    lower -=1
                    grid[1][i] = 1
        
        if upper != 0 or lower != 0:
            return []
        return grid
                
        