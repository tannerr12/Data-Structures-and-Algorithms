class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        h = Counter(words)
        
        #print(h)
        
       # doubled = defaultdict(int)
        
        
        s1, s2 = '' , ''
        remainder = 0
        
        for i in range(len(words)):
            word = words[i]
            back = word[::-1]
            
            if h[word] == 0:
                continue
            if word == back and h[word] >= 2:
                
                m = h[word] // 2
                
                s1 += word * m
                h[word] -= m
                s2 = (back * m) + s2
                h[back] -= m
                if h[word] == 1:
                    remainder = 2

            elif word == back and h[word] == 1:
                           
                    remainder = 2
            elif back in h and h[back] > 0:
                
                m = min(h[word], h[back])
                
                s1 += word * m
                h[word] -= m
                s2 = (back * m) + s2
                h[back] -= m 
                
            
            
        
        #for key 
        
       # print(doubled)
        #print(s1 + s2)
        
        #remainder = max(doubled.values())
        return len(s1) + len(s2) + remainder