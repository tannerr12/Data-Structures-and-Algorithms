class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
           
        starts = []
        ends = []
        
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    starts.append([i,j])
                elif grid[i][j] > 1:
                    for k in range(grid[i][j] -1):
                        ends.append([i,j])
                
            
        @cache
        def dfs(i, bitmap):
            
            if i >= len(starts):
                return 0
            
            res = float('inf')
            a,b = starts[i]
            for j in range(len(ends)):
                if bitmap & (1 << j) > 0:
                    continue
                x,y = ends[j]
                manhat = abs(a - x) + abs(b - y)
                res = min(res, dfs(i+1, bitmap | (1 << j)) + manhat)
            
            
            return res
        
        return dfs(0, 0)
            
        
            
        
        
                    
        
        
        