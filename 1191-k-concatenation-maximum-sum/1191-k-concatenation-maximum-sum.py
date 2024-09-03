class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        #find the best left and right position if we use all of K
        #not using all of K? we must be using 1 or 2
        #find the best sub array of both
        MOD = 10 ** 9 + 7
        if k >= 2:
            narr = arr + arr
        else:
            narr = arr
        curr = 0
        best = 0
        for i in range(len(narr)):
            curr += narr[i]
            curr = max(curr, 0)
            best = max(best, curr)
        
        return max(best, best + (sum(arr) * (k -2) if k > 2 else 0)) % MOD
        

        
        
        
        