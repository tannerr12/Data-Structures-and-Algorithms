class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        mp = defaultdict(lambda:defaultdict(int))
        for j in range(n):
            
            for i in range(m):
                
                val = grid[i][j]        
                mp[j][val] += 1
        
        
        #print(mp)
        
        @cache
        def dfs(i, last):
            
            if i >= n:
                return 0
            
            res = float('inf')
            for j in range(10):
                if j == last:
                    continue
                
                res = min(res, dfs(i+1, j) + (m - mp[i][j]))
            
            
            return res
        
        
        return dfs(0, -1)
                
                
                
                