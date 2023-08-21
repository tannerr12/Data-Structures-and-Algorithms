class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        for i in range(len(s)//2):
            
            new = s[:i+1] * (len(s) // (i+1))
            
            if new == s:
                return True
        
        return False