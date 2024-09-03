class Solution:
    def getLucky(self, st: str, k: int) -> int:
        
        s = ''
        
        for char in st:
            
            val = ord(char) - ord('a') + 1
            
            s += str(val)
            
            
        
        for i in range(k):
            cur = 0
            
            for char in s:
                cur += int(char)
            
            s = str(cur)
        
        
        return int(s)
                
            