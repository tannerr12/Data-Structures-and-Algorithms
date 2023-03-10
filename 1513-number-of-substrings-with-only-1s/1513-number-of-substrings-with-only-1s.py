class Solution:
    def numSub(self, s: str) -> int:
        
        
        #l = 0
        size = 0
        res = 0
        for i in range(len(s)):
            
            if s[i] == '1':
                size +=1
            
            else:
                res += (size * (size +1)) // 2
                size = 0
        
        if size:
            res += (size * (size +1)) // 2
        return res % (10 ** 9 + 7)