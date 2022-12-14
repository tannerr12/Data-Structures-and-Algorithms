class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        dp = [0] * (k +1)
        
        dp[0] = cookies[0]
        
        
        
        memo = {}
        
        
        def backtrack(i):
            
            if i >= len(cookies):
                
                return max(dp)

            if (i,str(dp)) in memo:
                return memo[(i,str(dp))]
            
            res = float('inf')
            for kid in range(k):
               
                dp[kid] += cookies[i]
                res = min(res,backtrack(i+1))
                dp[kid] -= cookies[i]
               
            memo[(i,str(dp))] = res
            return res
        
        
        return backtrack(1)
                
            
                