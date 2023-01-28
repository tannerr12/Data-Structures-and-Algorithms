class Solution:
    def countVowels(self, word: str) -> int:
        vowel = {'a','e','i','o','u'}
        
        N = len(word)

        
        
        total = 0
        
        for i,c in enumerate(word):
            if c in vowel:
            

                left = i + 1

                right = N - i

                total += left * right

                
                
        
        return total