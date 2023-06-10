class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def isGood(mid):
            
            leftMin = 0
            rightMin = 0
            if mid > index:
            #3 * (2 - 2 + 1) = 3  // 2
                leftMin = ((mid-1 + mid - index) * (mid-1 - (mid - index) + 1)) //2
            else:
                leftMin = ((mid-1 + 1) * (mid-1 - 1 + 1)) //2
                leftMin += index - mid +1

            if mid > (n - index -1):
                rightMin = ((mid-1 + mid - (n-index-1)) * (mid-1 - (mid - (n-index-1)) + 1)) //2
            else:
                rightMin = ((mid-1 + 1) * (mid-1 - 1 + 1)) //2
                rightMin += (n-index) - mid
                
            
            return leftMin + rightMin + mid <= maxSum
        
        l,r = 1, 10**9
        
        res = 0
        while l <= r:
            
            mid = (l+r) //2
            
            if isGood(mid):
                res = mid
                l = mid + 1
            
            else:
                r = mid -1
        
        
        return res
                