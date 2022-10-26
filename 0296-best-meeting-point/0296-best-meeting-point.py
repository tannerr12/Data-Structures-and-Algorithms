class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        
        row = []
        col = []
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        
        
        row.sort()
        col.sort()
        mr = row[len(row) // 2]
        mc = col[len(col) // 2]
        
        
        sr = 0
        sc = 0
        for r in row:

            sr += abs(r - mr)
            
        
        for c in col:
            sc += abs(c - mc)
            
        
        
        return sr + sc