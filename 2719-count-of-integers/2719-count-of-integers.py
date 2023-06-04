class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 **9 + 7


        @cache
        def dfs(idx,tight,sm):
            nonlocal s,min_sum,max_sum,MOD
      
            if idx == len(s):
                return sm <= max_sum and sm >= min_sum
            
            res = 0
            up = int(s[idx]) if tight else 9
                
            for i in range(up + 1):
                newsum = sm + i
                if newsum > max_sum:
                    break
                res += dfs(idx + 1, tight and i == up, newsum)
                res %= MOD
            
            return res % MOD
        
        
        s = num2
        #add the largest
        res = dfs(0,1,0)
        dfs.cache_clear()
        s = str(int(num1) -1)
        #sub the smallest
        res -= dfs(0,1,0)
        
        return res % MOD
                
                
        