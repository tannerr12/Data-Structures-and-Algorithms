class Solution:
    def breakPalindrome(self, pal: str) -> str:
        
        if len(pal) == 1:
            return ''
        
        pos = 0
        
        for i in range(len(pal)):
            
            #dont flip the middle character
            if i == len(pal) // 2 and len(pal) % 2:
                continue
                
            if pal[i] != 'a':
                new = pal[:i] + 'a' + pal[i+1:]
                return new
        
        
        return pal[:-1] + 'b' if pos >= 0 else '' 
            