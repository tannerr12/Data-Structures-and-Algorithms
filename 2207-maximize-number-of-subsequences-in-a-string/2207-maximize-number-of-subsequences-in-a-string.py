class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        if pattern[0] == pattern[1]:
            nxt = text.count(pattern[0]) 
            return nxt * (nxt + 1) // 2
        
        count = 0
        
        #always add the pattern[0] at the start or always add pattern[1] at the end 
        
        ntext = pattern[0] + text
        
        nxt = ntext.count(pattern[1])
        res = 0
        
        for i in range(len(ntext)):
            if ntext[i] == pattern[0]:
                res += nxt
            elif ntext[i] == pattern[1]:
                nxt -= 1
        
        
        ntext = text + pattern[1]
        
        nxt = ntext.count(pattern[1])
        ans = res
        res = 0
        
        for i in range(len(ntext)):
            if ntext[i] == pattern[0]:
                res += nxt
            elif ntext[i] == pattern[1]:
                nxt -= 1
        
        return max(ans,res)
            
        
        
        
        
                
            