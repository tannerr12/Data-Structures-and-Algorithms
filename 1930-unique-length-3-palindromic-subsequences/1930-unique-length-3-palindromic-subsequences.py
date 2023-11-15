class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        
        dpleft = [0] * len(s)
        dpright = [0] * len(s)
        left = 0
        right = 0
        
        for i in range(len(s)):
            
            dpleft[i] = left    
            left |= (1 << (ord(s[i]) - ord('a')))
            
        
        for i in range(len(s)-1,-1,-1):
            
            dpright[i] = right
            right |= (1 << (ord(s[i]) - ord('a')))
        
        
        seen = set()
        for num in range(1, len(s) -1):
            left = dpleft[num]
            right = dpright[num]
            for i in range(26):
            
                if left & (1 << i) > 0 and right & (1 << i) > 0:
                    val = chr(ord('a') + i)
                    seen.add(val + s[num] + val)
        
        return len(seen)
                    
            
