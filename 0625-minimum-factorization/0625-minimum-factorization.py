class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num == 1 or num == 0:
            return num
        mx = 2 ** 31 - 1
        
        
        factors = []
        n = num
        j = 2
        
        for j in range(2, 10):    
            while n % j == 0:
                factors.append(j)
                n //= j
            
            j += 1
        
        if n > 1:
            return 0
        
   
        
        factors = Counter(factors)
        
        for key,val in list(factors.items()):
            
            if key == 2:
                factors[8] += val // 3 
                val %= 3      
                factors[4] += val // 2
                val %= 2
                factors[2] = val
            
            if key == 3:
                
                factors[9] += val // 2
                val %= 2
                factors[3] = val
        
        
        if factors[3] > 0 and factors[2] > 0:
            mn = min(factors[2], factors[3])
            factors[6] += mn
            factors[3] -= mn
            factors[2] -= mn
        
        if factors[3] == 1 and factors[4] > 0:
            factors[3] -= 1
            factors[6] += 1
            factors[4] -= 1
            factors[2] += 1
        ans = ''
        for i in range(2, 10):
            ans += str(i) * factors[i]
        

        
        return int(ans) if int(ans) <= mx else 0
