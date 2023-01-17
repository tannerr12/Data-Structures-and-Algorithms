class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        prefix = [0] * len(s)
        if s[0] == '1':
            prefix[0] = 1
            
        for i in range(1,len(s)):
            if s[i] == '1':
                prefix[i] = prefix[i-1] + 1
            
            
            else:
                prefix[i] = prefix[i-1]
        
        sufix = [0] * len(s)
        if s[-1] == '0':
            sufix[0] = 1
        c = 1
        for i in range(len(s)-2,-1,-1):
            if s[i] == '0':
                sufix[c] = sufix[c-1] + 1
            
            
            else:
                sufix[c] = sufix[c-1]
            c+=1
    
       # print(prefix)
       # print(sufix)
        res = float('inf')
        for i in range(len(s)):
            res = min(res,prefix[i] + sufix[-(i +1)] -1)
            
        
        return res