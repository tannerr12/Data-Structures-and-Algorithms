class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        
        dp = [[float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
        mn1, mn2 = [float('inf'), 0], [float('inf'), 0]
        for j in range(len(grid[0])):
            dp[-1][j] = grid[-1][j]
            if dp[-1][j] <= mn1[0]:
                mn2 = mn1
                mn1 = [dp[-1][j], j]
            elif dp[-1][j] <= mn2[0]:
                mn2 = [dp[-1][j], j]
            
        for i in range(len(grid)-2,-1,-1):
            mn11, mn22 = [float('inf'), 0], [float('inf'), 0]
            for j in range(len(grid[0]) -1, -1,-1):
                
                if mn1[1] != j:
                    dp[i][j] = min(dp[i][j], mn1[0] + grid[i][j])
                elif mn2[1] != j:
                    dp[i][j] = min(dp[i][j], mn2[0] + grid[i][j])
                    
                if dp[i][j] <= mn11[0]:
                    mn22 = mn11
                    mn11 = [dp[i][j], j]
                elif dp[i][j] <= mn22[0]:
                    mn22 = [dp[i][j], j]   
                    
            mn1, mn2 = mn11,mn22
        
        return min(dp[0])
                
        '''
        rows = defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i].append((grid[i][j], j))
            
            rows[i].sort()

        q = deque()
        for val,idx in rows[0][:2]:
            q.append((val,1,idx))
    
        res = float('inf')
        while q:
            
            for i in range(len(q)):
                
                cost, x,y = q.popleft()
                
                if x == len(grid):
                    res = min(res,cost)
                    continue
         
                for val, idx in rows[x][:2]:
                    if idx != y:
                        q.append((cost + val, x+1, idx))
                        
                        
        
        return res
            
        
        '''
        
            
            