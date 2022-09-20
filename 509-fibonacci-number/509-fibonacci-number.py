class Solution:
    def fib(self, n: int) -> int:
        
        memo = {}
        def fib2(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            
            if n in memo:
                return memo[n]

            memo[n]  = fib2(n-1) + fib2(n-2)
            return memo[n]
        
        
        fib2(n)
        return memo[n] if n > 1 else  n