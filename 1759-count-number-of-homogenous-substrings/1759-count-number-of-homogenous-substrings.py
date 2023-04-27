class Solution:
    def countHomogenous(self, s: str) -> int:
        
        #count = Counter(s)
        res = 0
        MOD = 10 ** 9 + 7
        
        curChar = ''
        size = 0
    
        for i, e in enumerate(s):
            
            if e == curChar:
                size +=1
            else:
                if size > 0:
                    res += (size * (size + 1)) // 2
                    res %= MOD
                curChar = e
                size = 1
        
        
        return (res + (size * (size + 1)) // 2) % MOD
        
            
            
        