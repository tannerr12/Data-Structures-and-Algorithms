class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        dp = [0] * k
        
        def backtrack(i):
            
            if i >= len(cookies):
                #mn = min(dp)
                mx = max(dp)
                
                return mx
            
            res = float('inf')
            for kid in range(k):
                dp[kid] += cookies[i]
                res = min(res,backtrack(i+1))
                dp[kid] -= cookies[i]
                
            
            return res
        dp[0] += cookies[0]
        return backtrack(1)