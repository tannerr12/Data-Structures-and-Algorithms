class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        dash = s.count('-')
        
        chars = (len(s) - dash) % k
        
        #print(chars)
        res = []
        s = s.replace('-','')
        word = ''
        fword = ''
        start = 0
        if chars == 0:
            fword = s[:k]
            start = k
        else:
            fword = s[:chars]
            start = chars
        
        fword = fword.upper()
        res.append(fword)
        
        
        for i in range(start,len(s)):
            
            word += s[i].upper()
            
            if len(word) == k:
                res.append(word)
                word = ''
        
        
        #print(res)
        
        return '-'.join(res)