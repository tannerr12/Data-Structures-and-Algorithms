class Solution:
    def breakPalindrome(self, pal: str) -> str:
        
        pos = -1
        
        for i in range(len(pal)):
            
            #dont flip the middle character
            if i == len(pal) // 2 and len(pal) % 2:
                continue
            if pal[i] == 'a':
                pos = i
            else:
                new = pal[:i] + 'a' + pal[i+1:]
                return new
        
        
        return pal[:pos] + 'b' + pal[pos+1:] if pos >= 0 else '' 
            