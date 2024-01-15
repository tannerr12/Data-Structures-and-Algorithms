class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        h = {}

        for i in range(len(keyboard)):
            h[keyboard[i]] = i
        

        res = 0
        pos = 0
        prev = 0
        for i in range(len(word)):
            res += abs(prev - h[word[i]])
            prev = h[word[i]]
        
        return res