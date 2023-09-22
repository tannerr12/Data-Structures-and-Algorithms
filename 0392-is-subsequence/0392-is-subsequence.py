class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        c = 0
        
        for i in range(len(t)):

            if s[c] == t[i]:
                c+=1
                
            if c == len(s):
                return True


        
        return False
        
        