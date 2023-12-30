class Solution:
    def smallestNumber(self, n: int) -> str:
        
        
        factors = []
        orgn = n
        if n < 10:
            return str(n)
        
        for i in range(9, 1, -1):

            while n % i == 0:
                factors.append(str(i))
                n //= i
        
        
        if n > 1:
            return str(-1)
        #print(factors)
        factors = factors[::-1]
        
        return ''.join(factors)