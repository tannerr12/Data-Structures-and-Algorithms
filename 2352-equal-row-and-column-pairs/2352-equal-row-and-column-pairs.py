class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        col = defaultdict(int)
        row = defaultdict(int)
        for i in range(len(grid)):
            arr = []
            for j in range(len(grid[0])):
                
                val = grid[i][j]
                
                arr.append(val)
            
            col[tuple(arr)] +=1
        
        
        for j in range(len(grid[0])):
            arr = []
            for i in range(len(grid)):
                val = grid[i][j]
                arr.append(val)
                
            row[tuple(arr)] +=1
        
        res = 0
        for key,val in row.items():
            if key in col:
                res += val * col[key]
                
        
        return res
            
                