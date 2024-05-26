class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
        word = []
        for i in range(len(s)):
            
            distA = ord(s[i]) - ord('a')
            distAR = (26 + ord('a')) - ord(s[i])
            dist = min(distA, distAR)
            if k >= dist:
                word.append('a')
                k -= dist
            else:
                word.append(chr(ord(s[i]) - k))
                k = 0
                
        
        return ''.join(word)
            