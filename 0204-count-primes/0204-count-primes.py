class Solution:
    def countPrimes(self, n: int) -> int:
        p = set()
        primes = []
        def getPrimes(n):
            
            isPrime = [True] * n
            isPrime[0] = False
            isPrime[1] = False
            for i in range(2, isqrt(n)+1):
                for x in range(i*i, n, i):
                    isPrime[x] = False
            
            
            res = []
            for i,e in enumerate(isPrime):
                if e == True:
                    res.append(i)
            
            return res
        
        if n < 2:
            return 0
        return len(getPrimes(n))
        
        
            