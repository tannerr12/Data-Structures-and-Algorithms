class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        n+=1
        left = [0] * n
        right = [0] * n
        dic = set(cuts)
        last = -1
        for i in range(n):
            if i in dic:
                last = i
            
            left[i] = last
        
        last = n + 1
        
        for i in range(n-1,-1,-1):
            if i in dic:
                last = i
            
            right[i] = last
        
        @cache
        def divide(i, j):
            nonlocal left,right

            if j - i + 1 <= 2 or (left[j-1] <= i or right[i + 1] >= j):
                return 0

            val = right[i + 1]
            cost = float('inf')
            while val < j:
                l = divide(i, val) 
                r = divide(val, j)
                cost = min(cost, l + r)
                val = right[val +1]
            
            res = cost + (j - i)
            return res
        
        return divide(0,n-1)