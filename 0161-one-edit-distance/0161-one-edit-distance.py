class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        
        if len(s) == len(t):
            diff = 0
            for i in range(len(s)):
                
                if s[i] != t[i]:
                    diff+=1
                
            
            return diff == 1
        
        if len(t) < len(s):
            s,t = t,s
        i,j = 0,0
        diff = 0
        while i < len(s) and j < len(t):

            if s[i] != t[j]:
                j+=1
                diff +=1

            else:
                i+=1
                j+=1

        if j < len(t):
            diff += len(t) - j

        return diff == 1



            
        