class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        
        #find prime factors than calculate abs, if any 2 primes are the same return those results
    
        
        n1 = num + 1
        n2 = num + 2
        
        """
        def factorize(n):
            j = 2
            primes = []
            while j < n and n != 1:
                if n % j == 0:
                    primes.append(j)
                    #n //= j
            
                j+= 1 + j % 2
            #if n > 1:
             #   primes.append(j)
            
            return primes
        """
       
        #count divisors from both ends of the number and go inwards get the distance between the left and right
        #we can assume if i goes into N than n // i will also be divisable
        best = float('inf')
        ans = []
        def factors(n):  
            nonlocal best
            nonlocal ans
            i = 1
            #sqrt of n is highest #
            while i * i <= n:
                if n % i == 0:
                    current = abs(i-n//i)
                    if current < best:
                        best = current
                        ans = [i, n//i]
                
                i+=1
            
            
        factors(n1)
        factors(n2)
        
        return ans
        """
        primes.sort()
        
        res = float('inf')
        for i in range(1,len(primes)):
            
            res = min(res, primes[i] - primes[i-1])
        
        
        
        for i in range(1,len(primes)):
            
            if primes[i] - primes[i-1] == res:
                return [primes[i-1], primes[i]]  
                
        """