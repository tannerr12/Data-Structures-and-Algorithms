class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    rows[i].add((i,j))
                    cols[j].add((i,j))
        
        
        res = set()
        
        for key,val in rows.items():
            if len(val) > 1:
                res = res | val
        for key,val in cols.items():
            if len(val) > 1:
                res = res | val
        
        #print(res)
            
            
        return len(res)
    