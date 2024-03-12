class Solution:
    def breakPalindrome(self, pal: str) -> str:
        
        cur = 0
        pos = -1
        
        for i in range(len(pal)):
            if i == len(pal) // 2 and len(pal) % 2:
                continue
            if pal[i] == 'a':
                cur = 1
                pos = i
            else:
                new = pal[:i] + 'a' + pal[i+1:]
                return new
        
        
        if pos == -1:
            return ''
        
        new = pal[:pos] + 'b' + pal[pos+1:]
        return new 
            