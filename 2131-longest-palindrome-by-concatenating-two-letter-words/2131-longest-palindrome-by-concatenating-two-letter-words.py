class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        h = Counter(words)

        res = 0
        remainder = 0
        
        for i in range(len(words)):
            word = words[i]
            back = word[::-1]
            
            if h[word] == 0:
                continue
            if word == back and h[word] >= 2:
                
                m = h[word] // 2
                h[word] -= m * 2
                res += 2 * (m*2)
                if h[word] == 1:
                    remainder = 2

            elif word == back and h[word] == 1:  
                remainder = 2
            elif back in h and h[back] > 0:
                
                m = min(h[word], h[back])
                h[word] -= m
                h[back] -= m
                
                res += 2 * (m*2)
                
            
        
        return res + remainder