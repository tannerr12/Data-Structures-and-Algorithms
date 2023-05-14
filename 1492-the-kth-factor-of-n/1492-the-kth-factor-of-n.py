class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        factors = []
        i = 1
        sqr = sqrt(n)
        while i <= sqr:
            if n % i == 0:
                factors.append(i)
                k-=1
                if k == 0:
                    return i
                if i == sqr:
                    k+=1

            i +=1
        
        if k > len(factors):
            return -1
        else:
            val = n // factors[-k]
            return val