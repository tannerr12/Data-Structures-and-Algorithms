class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
       
    
    
        return False
    '''
        
        l = 2
        r = len(s)-1
        
        while l < r:
            
            if s[l] != s[r]:
                return False
            
            l+=1
            r-=1
            
        return True 
        
    '''