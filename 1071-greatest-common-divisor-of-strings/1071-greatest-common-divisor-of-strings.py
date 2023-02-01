class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ''
        for i in range(min(len(str1), len(str2))):
            
            char = str1[:i+1]
            last = 0
            found = True
            for j in range(len(char),len(str1), len(char)):
                
                if str1[last:j] != char:
                    found = False
                    break
                
                last = j
            
            if last != len(str1) and str1[last:] != char:
                found = False
            
            last = 0
            for j in range(len(char),len(str2), len(char)):
                
                if str2[last:j] != char:
                    found = False
                    break
                
                last = j
                
            if last != len(str2) and str2[last:] != char:
                found = False
            
            if found:
                res = char
    
    
        
        return res
            
            
                       
                       