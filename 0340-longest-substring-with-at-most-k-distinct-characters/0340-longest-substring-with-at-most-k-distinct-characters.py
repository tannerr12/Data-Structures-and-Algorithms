class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        if k == 0:
            return 0
        h= {}
        
        res = 0
        
        
        l = 0
        i = 0
        while i < len(s):
            
            if len(h) < k or s[i] in h and len(h) == k:
                
                
                if s[i] in h:
                  
                    h[s[i]] +=1
                else:
                   
                    h[s[i]] = 1
                    
                res = max(res,i+1 - l)
                i+=1
                
            else:
                        
                h[s[l]] -=1
                
                if h[s[l]] == 0:
                    del h[s[l]]
                    
                l+=1
        
        
        return res
            
        
        