class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        r = 0
        
        for i in range(len(s)):
            if r >= len(t):
                break
            if t[r] == s[i]:
                r+=1
                
        
        return len(t) - r