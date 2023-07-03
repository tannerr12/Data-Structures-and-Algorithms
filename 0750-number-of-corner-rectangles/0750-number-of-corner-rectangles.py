class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        
        pairs = defaultdict(int)
        res = 0
        for i in range(len(grid)):
            ones = []
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if len(ones) > 0:
                        for val in ones:
                            res += pairs[(val,j)]
                            pairs[(val,j)] += 1
                            
                    
                    ones.append(j)
        
        return res
                    
                    
                    