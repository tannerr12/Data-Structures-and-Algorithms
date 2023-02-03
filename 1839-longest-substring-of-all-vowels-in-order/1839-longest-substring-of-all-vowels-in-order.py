class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
       # v = {'a':0,'e':1,'i':2,'o':3,'u':4}
        
        l = 0
        vowel = {}
        res = 0
        last = word[0]
        vowel[word[0]] =1
        for i in range(1,len(word)):
        
            if word[i] in vowel:
                vowel[word[i]] += 1
            else:
                vowel[word[i]] = 1
                
            if word[i] < last:
                vowel = {}
                vowel[word[i]] = 1
                l = i
                
            
            last = word[i]
            if len(vowel) == 5:
                res = max(res, i-l +1)
        
        return res
            