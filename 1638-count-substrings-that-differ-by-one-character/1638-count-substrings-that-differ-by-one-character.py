
        

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
  
        res =0
        for i in range(len(s)):
            for j in range(len(t)):
                
                x,y = i, j
                count = 0
                while x < len(s) and y < len(t):
                    
                    if s[x] != t[y]:
                        count +=1
                    if count ==1:
                        res +=1
                    if count == 2:
                        break
                    
                    x+=1
                    y+=1
        
        return res
                    
        