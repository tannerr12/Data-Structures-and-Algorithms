class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        primes = 4
        evens = 5
        
        ecount = n//2
        total = pow(primes,ecount,MOD)
        total *= pow(evens,ecount,MOD)

        if n % 2:
            total = (total * 5) % MOD
        
        
        return total % MOD