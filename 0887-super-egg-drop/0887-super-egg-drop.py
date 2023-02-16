class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """  
        @lru_cache(None)
        def dp(k,n):
            if n == 0:
                return 0
            if k == 1:
                return n
                   
            l,r = 1, n
            
            while l < r:
                
                mid = (l + r) // 2
                breakk = dp(k - 1,mid - 1)
                nobreak = dp(k, n-mid)
                
                if breakk < nobreak:
                    l = mid +1
                else:
                    r = mid
            
            res = float('inf')
            res = min(res, 1 + max(dp(k - 1, l - 1), dp(k, n-l))) # min-max
            return res 
            
        return dp(k,n)
        """
        
        dp = range(n + 1)
        
        for i in range(2, k +1):
            
            dp2 = [0]
            x = 1
            for j in range(1,n+1):
                
                
                while x < n and max(dp[x-1], dp2[j-x]) > max(dp[x], dp2[j-x-1]):
                    x+=1
                
                
                dp2.append(1 + max(dp[x-1], dp2[j-x]))
            
            
            dp = dp2
        
        return dp[-1]