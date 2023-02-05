class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # count all of the characters and when the number of character is the same as the target add the 
        #left point index to an array
        # left and right index should always be len(p) appart
        # we can also use an array of size 26 for each character

        res = []
        if len(p) > len(s):
            return res
        letterS = [0] * 26
        letterP = [0] * 26
        r = len(p) -1
        for i in range(len(p)):
            
            letterS[ord(s[i]) - ord('a')] += 1
            letterP[ord(p[i]) - ord('a')] += 1
        
        
        for i in range(len(s)):
            if letterS == letterP:
                res.append(i)
            if r == len(s) -1:
                break
            r+=1
            letterS[ord(s[i]) - ord('a')] -= 1
            letterS[ord(s[r]) - ord('a')] += 1
        return res
            
            
        
        
        