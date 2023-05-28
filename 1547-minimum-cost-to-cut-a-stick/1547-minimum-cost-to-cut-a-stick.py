class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        n+=1
        cuts.sort()
        left = [0] * n
        right = [0] * n
        dic = set(cuts)
        last = -1
        for i in range(n):
            if i in dic:
                last = i
            
            left[i] = last
        
        last = n + 2
        
        arr = [i for i in range(n)]
        for i in range(n-1,-1,-1):
            if i in dic:
                last = i
            
            right[i] = last
        
        @cache
        def divide(i, j):
            nonlocal left,right,arr

            if j - i + 1 <= 2 or (left[arr[j] -1] <= arr[i] or right[arr[i] + 1] >= arr[j]):
                return 0
            
            
            val = right[arr[i] + 1]
            cost = float('inf')
            while val < arr[j]:
                l = divide(i, val) 
                r = divide(val, j)
                cost = min(cost, l + r)
                val = right[val +1]
            
            res = cost + (j - i)
            
            return res
        
        return divide(0,len(arr)-1)