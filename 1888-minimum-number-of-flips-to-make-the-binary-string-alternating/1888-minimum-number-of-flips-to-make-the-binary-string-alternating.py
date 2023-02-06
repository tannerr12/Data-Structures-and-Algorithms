class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        one = []
        zero =[]
        
        for i in range(len(s)):
            
            if i % 2:
                one += '1'
                zero += '0'
            else:
                one += '0'
                zero += '1'
            
        diff1 = 0
        diff2 = 0
        res = float('inf')
        l=0
        for i in range(len(s)):
            
            if s[i] != one[i]:
                diff1 +=1
            if s[i] != zero[i]:
                diff2 +=1
            
            if i - l + 1 > n:
                if s[l] != one[l]:
                    diff1 -= 1
                
                if s[l] != zero[l]:
                    diff2 -=1
                l +=1
            
            if i - l + 1 == n:
                res = min(res, diff1,diff2)
            
        
        
        return res
            
            