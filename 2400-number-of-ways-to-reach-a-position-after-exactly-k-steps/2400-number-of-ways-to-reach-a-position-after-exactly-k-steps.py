class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        
        if abs(endPos - startPos) > k:
            return 0
        
        if abs(endPos - startPos) % 2 != k % 2:
            return 0
        
        
        
        #gap = abs(endPos - startPos)
        
        #right = k - gap
        
        
        
        #return left % (10**9 + 7)
        
        @cache
        def dp(i, steps):
            
            
            if abs(endPos - i) > steps:
                return 0
            
            if steps == abs(endPos - i):
                return 1
            
            
            res = 0
            #step left
            res += dp(i-1,steps -1)
            
            #step right
            res += dp(i+1, steps -1)
            
            
            
            return res
        
        
        return dp(startPos, k) % (10**9 + 7)
            