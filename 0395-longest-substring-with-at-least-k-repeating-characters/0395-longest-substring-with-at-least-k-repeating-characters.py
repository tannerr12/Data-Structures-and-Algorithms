class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
  
        if k > len(s):
            return 0
    
        h = Counter(s)
        res = 0

        
        
        for char,occurance in h.items():
            
            if occurance  < k:
                
                m = 0
                for c in s.split(char):
                    m = max(m,self.longestSubstring(c,k))
                    
                return m
            
        
        
        
        return len(s)
        