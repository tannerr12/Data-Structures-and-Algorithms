class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        


        @cache
        def divide(s1, s2):
            if s1 == s2:
                return True
            if len(s1) == 1:
                return s1 == s2
            
            n = len(s1)
            for i in range(1,n):
                
                if (divide(s1[:i],s2[:i]) and divide(s1[i:],s2[i:])) or (divide(s1[:i],s2[n-i:]) and divide(s1[i:],s2[:n-i])):
                    return True
            
            
            return False
    
        
        return divide(s1,s2)
    