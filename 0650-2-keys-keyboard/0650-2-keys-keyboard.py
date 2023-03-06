class Solution:
    def minSteps(self, n: int) -> int:
        """
        i = 2
        res = 1
        
        while n != 0 and i < 1000:
            if n % i == 0:
                res +=1
            
            while n % i == 0:
                n //= i
                res +=1
            
            
            i += 1 + i % 2
        
        
        return res
        """
        if n == 1:
            return 0
        if n == 2:
            return 2
        
        
        def dfs(count, cur):
            
            if count == n:
                return 0
            elif count > n:
                return float('inf')
        
            res = float('inf')
            #take 
            res = min(res,dfs(count * 2, count) + 2)
            #dont take
            res = min(res,dfs(count + cur, cur) + 1)
            
            return res
        
        
        return dfs(2, 1) + 2
            
            