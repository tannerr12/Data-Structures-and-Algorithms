class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        
        dp = [[float('inf') for j in range(len(grid[0]))] for i in range(len(grid))]
        
        for j in range(len(grid[0])):
            dp[-1][j] = grid[-1][j]
        for i in range(len(grid)-2,-1,-1):
            for j in range(len(grid[0]) -1, -1,-1):
                
                for k in range(len(dp[0])):
                    if k == j:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i+1][k] + grid[i][j])
        
        
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
        
            
            