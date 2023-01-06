class Solution:
    def countSpecialNumbers(self, n: int) -> int:  
        
        
        @cache
        def dfs(i, prefix, bitmask,n):
            start = 0
            if i == 0:
                start = 1
            
            if i >= len(n):
                return 1
            res = 0
            for j in range(start ,10):
                
                if prefix and j > int(n[i]):
                    break
                    
                if bitmask & (1 << j):
                    continue
                    
            
                res  += dfs(i+1, prefix and j == int(n[i]), bitmask | (1 << j),n)
            
            return res
        
        
        res = dfs(0,True,0,str(n))
        
        for i in range(1, len(str(n))):
            
            al = '9' * i
            res += dfs(0,True,0,al)
        
        
        return res
        
        
            