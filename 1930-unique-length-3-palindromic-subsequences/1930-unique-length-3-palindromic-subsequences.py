class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
    
        dpright = [0] * len(s)
        right = 0
        
        left =set()
            
        
        for i in range(len(s)-1,-1,-1):
            
            dpright[i] = right
            right |= (1 << (ord(s[i]) - ord('a')))
        
        
        seen = set()
        for num in range(len(s) -1):
            right = dpright[num]
            for i in range(26):
                val = chr(ord('a') + i)
                if right & (1 << i) > 0 and val in left:
                    
                    seen.add(val + s[num] + val)
            left.add(s[num])
        return len(seen)
                    
            
