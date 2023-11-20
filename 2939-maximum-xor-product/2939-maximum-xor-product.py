class Solution:
    def maximumXorProduct(self, x: int, y: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        #if there are positions with 0:0 we should always turn those on
        #if there are postions with 1:1 we should never turn those on
        #if there are postions with 1:0 we should attempt on or off
        
        #orr = a | b
        
      
        def dfs(a,b,i):
            
            if i < 0:                
                return (a * b) 
            
            
        
            onA = a & (1 << i) > 0
            onB = b & (1 << i) > 0
            res = 0
            if onA and onB:
                res = max(res, dfs(a,b, i - 1)) 
            elif not onA and not onB:
                res = max(res, dfs(a | (1 << i),b | (1 << i), i-1)) 
            elif onA:
                
                if a > b:
                    #0
                    res = max(res, dfs(a ^ (1 << i),b | (1 << i), i-1))             
                else:
                    res = max(res, dfs(a,b, i - 1)) 
            else:
                if a > b:
                    #b - > 1 a -> 0 -> 0 1 ^ 0 = 1 0 ^ 0 = 1
                    res = max(res, dfs(a,b, i-1))             
                else:
                    res = max(res, dfs(a | (1 << i),b ^ (1 << i), i - 1)) 
                
            
            return res 
        
        return dfs(x,y, n-1) % MOD
        
   
                
            
     