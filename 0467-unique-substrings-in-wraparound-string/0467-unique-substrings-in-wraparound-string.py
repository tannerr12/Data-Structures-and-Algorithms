class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        
        
        l = 1
        countMp = defaultdict(int)
        countMp[s[0]] =1
        
        for i in range(1, len(s)):
            
            if ord(s[i-1]) == ord(s[i]) -1 or s[i-1] == 'z' and s[i] == 'a':
                l +=1
            else:
                l = 1
            
            
            countMp[s[i]] = max(countMp[s[i]], l)
        
        
        return sum(countMp.values())
        
        
            
            