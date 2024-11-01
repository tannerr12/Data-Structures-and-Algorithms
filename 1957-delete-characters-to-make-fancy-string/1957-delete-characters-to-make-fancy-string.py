class Solution:
    def makeFancyString(self, s: str) -> str:
        
        res = 0
        count = 0
        last = ''
        ans = []
        for i in range(len(s)):
            char = s[i]
            
            if char == last:
                count += 1
                
            else:
                count = 1
                last = char
            
            
            if count < 3:
                ans.append(char)
        
        
        
        return ''.join(ans)