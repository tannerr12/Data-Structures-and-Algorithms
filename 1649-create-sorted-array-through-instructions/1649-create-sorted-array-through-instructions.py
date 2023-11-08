
class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        
        m = max(A)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                #add lsb
                x += x & -x

        def get(x):
            res = 0
            #x is the bit
            while (x > 0):
                #add parnet
                res += c[x]
                #remove lsb
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10**9 + 7)