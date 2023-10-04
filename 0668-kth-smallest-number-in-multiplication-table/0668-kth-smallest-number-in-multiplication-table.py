class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        #search right so find range where the max multiplication is > 
        
        # 9 3 * 3
        # 2 * 4
        # 1 * 9 
        
        # 3 + 4 + 9 = 16th smallest number search left
        
        
        def isGood(mid):
            less = 0
            sameCount = 0
            for i in range(1,m + 1):
                less += min(n, mid // i)
                
                if mid // i <= n and mid % i == 0:
                    sameCount += 1
            
            return less+1 > k,less+1-sameCount <= k and less >= k
                
            
            
        l, r = 1, m*n
    
        while l <= r: 
            
            mid = (l + r) // 2
            x,y = isGood(mid)
            if x and not y:
                r = mid - 1
            elif not x and not y:
                l = mid + 1
            else:
                return mid
            
        return l
            
        