class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        res = True
        
        lower = not word[0].isupper()
        second = False
        for i in range(1, len(word)):
            
            if lower and word[i].isupper() or second and word[i].islower():
                return False
            if word[i].isupper():
                second = True
            if not lower and word[i].islower():
                lower = True
        
        
        return res