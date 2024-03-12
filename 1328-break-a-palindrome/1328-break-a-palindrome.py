class Solution:
    def breakPalindrome(self, pal: str) -> str:
        
        best = '}'
        for i in range(len(pal)):
            if i == len(pal) // 2 and len(pal) % 2:
                continue
            if pal[i] == 'a':
                new = pal[:i] + 'b' + pal[i+1:]
                best = min(best,new)
            else:
                new = pal[:i] + 'a' + pal[i+1:]
                best = min(best,new)
        
        return best if best != '}' else ''
            