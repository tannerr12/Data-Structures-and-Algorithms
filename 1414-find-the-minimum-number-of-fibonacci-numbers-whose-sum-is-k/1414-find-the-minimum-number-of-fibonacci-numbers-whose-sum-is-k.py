class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        res = []
        @cache
        def fib(n):
            
            if n==0:
                res.append(1)
                return 1
            if n == 1:
                res.append(1)
                return 1
            
            v = fib(n-1) + fib(n-2)
            if v <= k:
                res.append(v)
            return v
        
        
        fib(45)
        curr = 0
       
        for i in range(len(res)-1,-1,-1):
            if res[i] <= k:
                k -= res[i]
                curr +=1
        
        return curr