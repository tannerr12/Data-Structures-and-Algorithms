class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        
        chars = 0
        
        for i in range(len(s)):
            
            if s[i].isalpha():
                chars += 1
                
            else:
                chars += (chars) * (int(s[i]) -1)
            
            
        
        for c in reversed(s):
            k %= chars
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                chars /= int(c)
            
            else:
                chars -= 1
        
        
        
        
        
        