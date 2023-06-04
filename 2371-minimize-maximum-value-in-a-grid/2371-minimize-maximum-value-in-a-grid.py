class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        def oob(i,j):
            nonlocal m,n
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            return True
        
        m,n = len(grid), len(grid[0])
        
        row = defaultdict(int)
        col = defaultdict(int)
        heap = []
        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                heap.append((curr, i,j))

        heap.sort()
        
        for i in range(len(heap)):
            val, j, k = heap[i]
            if row[j] == 0:
                row[j] = 1
            if col[k] == 0:
                col[k] = 1
            v = max(row[j], col[k])

            row[j] = v + 1
            col[k] = v + 1
            grid[j][k] = v
        
        return grid
                
        
        '''
        def updateGrid(grid):
            nonlocal m,n
            for i in range(m):
                for j in range(n):
                    curr = grid[i][j]
                    val = 1
                    if oob(i+1,j):
                        if grid[i+1][j] < curr:
                            val = max(val, grid[i+1][j] +1)
                    if oob(i,j+1):
                        if grid[i][j+1] < curr:
                            val = max(val, grid[i][j+1] +1)
                    if oob(i,j-1):
                        if grid[i][j-1] < curr:
                            val = max(val, grid[i][j - 1] +1)
                    if oob(i-1,j):
                        if grid[i-1][j] < curr:
                            val = max(val, grid[i-1][j] +1)

                    grid[i][j] = val
        
        
            return grid 
        
        
        for i in range(10):
            updateGrid(grid)
        
        return grid
        
        '''