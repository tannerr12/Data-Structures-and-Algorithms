class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        if len(houses) == k:
            return 0
        
        houses.sort()
        n = len(houses)
        cost = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                medianPos = houses[(i + j) // 2]     
                for m in range(i, j+1):
                    cost[i][j] += abs(medianPos - houses[m])
        
        
        @cache
        def dfs(i,k):
            
            nonlocal n
            if i == n and k == 0:
                return 0
            if i == n or k == 0:
                return float('inf')
            
            res = float('inf')
            for j in range(i, n):
       
                res = min(res, dfs(j+1, k-1) + cost[i][j])
            
    
            return res
        
        
        return dfs(0, k)
            
            
            
