class Solution:
    def convertToTitle(self, n: int) -> str:
        
        res = ""
        while n > 0:
            r = (n-1) % 26
            n = (n-1)// 26
            res += chr(ord("A")+r)
        return res[::-1]
            
            
                
                    
                    
            