class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        #at any left point our count is 0 
        #at any right point it must be even
        
        #the difference will be the binary of right and left
        
        #left
        #01100 -> 2 odds
        #01100 -> 2 odds
        #^
        #00000
        
        #at any perfix we need to find the rightmost prefix
        
        nummap = defaultdict(int)
        num = 0
        
        vowel = {'a':0,'e':1,'i':2,'o':3,'u':4}
        for i in range(len(s)):
            
            if s[i] in vowel:
                num ^= (1 << vowel[s[i]])
            
            nummap[num] = i
            
        
        num = 0
        #print(nummap)
        res = 0
        for i in range(len(s)):
            
            if num in nummap:
                res = max(res, nummap[num] - i + 1)
            if s[i] in vowel:
                num ^= (1 << vowel[s[i]])
            
            
            
        
        return res
            
            
        
        
        