class Solution:
    def reverseVowels(self, s: str) -> str:
    
        v = set(['a','e','i','o','u'])
        
        left, right = '',''
        
        l,r = 0,len(s) -1
        
        while l < r:
            if s[l].lower() not in v:
                left += s[l]
                l+=1
            elif s[r].lower() not in v:
                right = s[r] + right
                r -=1
                
            else:
                right = s[l] + right
                l+=1
                
                left += s[r]
                r -=1
        
        res = left + right
        
        return res if len(res) == len(s) else left + s[l] + right
                
            
                
            
                
            