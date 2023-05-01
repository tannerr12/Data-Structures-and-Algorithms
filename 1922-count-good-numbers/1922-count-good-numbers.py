class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        primes = 4
        evens = 5
        
        ecount = n//2
        total = pow(primes,ecount,MOD)
        total *= pow(evens,ecount + n % 2,MOD)        
        
        return total % MOD