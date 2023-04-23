class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        '''
        1,1,1
        1,1,0
        1,1,1
        0,1,1
        1,1,1
        
        
        super tedious problem but the idea is to keep a prefix sum map to each row and column for vertical and horizontal outside edges 
        than each time we see a one we go through the top and left layers until we no longer see 1s and use our prefix array to verify that all the
        outter edges are also ones and if valid res = (depth+1) ** 2
        '''
        
        
        
        m,n = len(grid), len(grid[0])
        col = defaultdict(list)
        row = defaultdict(list)
        
        for i in range(m):
            
            for j in range(n):
                if j not in col:
                    col[j].append(0)
                if i not in row:
                    row[i].append(0)
                    
                col[j].append(grid[i][j] + col[j][-1])
                row[i].append(grid[i][j] + row[i][-1])
                
        

        res = 0
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    res = max(res,1)
                    k = 1
                    #ones
                    while i+k < m and grid[i+k][j] == 1 and j + k < n and grid[i][j+k] == 1:
                        #we need to check prefix
                        csum = col[j+k][i+k+1] - col[j + k][i]
                        rsum = row[i+k][j+k+1] - row[i+k][j]
                        
                        if csum == k+1 and rsum == k+1:
                            res = max(res, (k + 1) ** 2)
                        k += 1
                    
                    
        return res