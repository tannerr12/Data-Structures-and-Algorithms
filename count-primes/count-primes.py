class Solution:
    def countPrimes(self, n: int) -> int:
        p = set()
        primes = []
        def getPrimes(n):
            count = n -2
            isPrime = [True] * n
            isPrime[0] = False
            isPrime[1] = False
            for i in range(2, isqrt(n)+1):
                for x in range(i*i, n, i):
                    if isPrime[x]:
                        count -=1
                    isPrime[x] = False
    
            
            return count
        
        if n < 2:
            return 0
        return getPrimes(n)
        
        
            