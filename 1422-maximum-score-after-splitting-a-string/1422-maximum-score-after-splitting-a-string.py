class Solution:
    def maxScore(self, s: str) -> int:
    
        one = 0
        zero = 0
        for i in range(len(s)):
            if s[i] == '1':
                one += 1
            
    
        res = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1
            
            res = max(res, zero + one)
    
        
        return res
            
        