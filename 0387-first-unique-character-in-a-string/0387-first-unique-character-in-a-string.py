class Solution:
    def firstUniqChar(self, s: str) -> int:
        h= collections.defaultdict(int)
        for i in range(len(s)):
            
            h[s[i]] +=1
            
        
        
        for i in range(len(s)):
            
            if h[s[i]] == 1:
                return i
        
        
        return -1
            
            
            