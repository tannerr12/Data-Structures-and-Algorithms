class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = defaultdict(int)
        cols = defaultdict(int)
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    rows[i] +=1
                    cols[j] +=1
        
        
        res = 0
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        res +=1
        
        return res
        
        """
        res = set()
        
        for key,val in rows.items():
            if len(val) > 1:
                res = res | val
        for key,val in cols.items():
            if len(val) > 1:
                res = res | val
        
        #print(res)
            
        """
