class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        count = {}
        res = 0
        l = 0
        for i in range(len(s)):
            
            if s[i] in count:
                count[s[i]] +=1
            else:
                count[s[i]] =1
                
            
            while len(count) > 2:
                
                count[s[l]] -=1
                if count[s[l]] == 0:
                    del count[s[l]]
                
                l +=1
            
            
            res = max(res, i - l + 1)
        
        
        return res
                