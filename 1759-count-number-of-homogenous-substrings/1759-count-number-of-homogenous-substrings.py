class Solution:
    def countHomogenous(self, s: str) -> int:
        
        #count = Counter(s)
        res = 0
        MOD = 10 ** 9 + 7
        size = 1
    
        for i in range(1,len(s)):
            
            if s[i] == s[i-1]:
                size +=1
            else:
                res += (size * (size + 1)) // 2
                res %= MOD
                size = 1
        
        
        return (res + (size * (size + 1)) // 2) % MOD
        
            
            
        