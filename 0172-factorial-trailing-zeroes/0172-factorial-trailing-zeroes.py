class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        num = str(math.factorial(n))
        
       #print(len(num))
        
        res = 0
        i = len(num) -1
        while num[i] == '0':
            res +=1
            i-=1
        return res