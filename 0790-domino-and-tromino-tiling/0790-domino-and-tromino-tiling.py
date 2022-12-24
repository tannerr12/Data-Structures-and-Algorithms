class Solution:
    def numTilings(self, n: int) -> int:
        
        mod = 10 ** 9 + 7
        
        @cache
        def p(n):
            if n == 2:
                return 1
            return (p(n -1) + f(n - 2)) 
        
        
        @cache
        def f(n):
            if n<=2:
                return n
            return (f(n-1) + f(n-2) + 2 * p(n-1))
        
        
        return f(n) % mod