class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowel = set(['a','e','i','o','u'])
        
        l = 0
        count = 0
        res = 0
        for i in range(len(s)):
            char = s[i]
            
            if char in vowel:
                count +=1
            
            
            while i - l + 1 > k:
                
                charL = s[l]
                if charL in vowel:
                    count -=1
                
                l+=1
            
            if i - l + 1 == k:
                res = max(res, count)
                
        
        
        return res
            
            