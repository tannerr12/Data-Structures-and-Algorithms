class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        
        dp = [[0 for j in range(n)] for i in range(n)]
        
        
        for s1,e1,s2,e2 in queries:
            for r in range(s1, s2 +1):
                dp[r][e1] +=1
                if e2 + 1 < n:
                    dp[r][e2 + 1] -=1
        
    
        
    
        for r in range(n):
            for c in range(1,n):
                dp[r][c] += dp[r][c-1] 
        
        
        return dp