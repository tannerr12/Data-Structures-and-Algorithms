class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            
            rep = 0
            end = True
            for j in range(i+1, len(s)):
                
                if s[j] == s[j-1]:
                    rep +=1
                    if rep == 2:
                        end = False  
                        res = max(res, j - i)
                        break
            
            if end:
                res = max(res, len(s) - i)
        
        return res
                
            