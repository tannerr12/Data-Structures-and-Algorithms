class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        
        #count numbers from 0 -> mid that are divisable by a
        #do the same for b
        #count ones that overlap (LCM)
        #add step 1 + step 2 - step 3
        #through binary seach see if target is greater less or equal to n
        
        MOD = 10 ** 9 + 7
        
        G = lcm(a,b)
        def isGood(mid):
            v1 = mid // a
            v2 = mid // b
            v3 = mid // G
            
            return [v1 + v2 - v3 < n, v1 + v2 - v3 == n]
            
            
        l, r = 0, 10 ** 15
        res = 0
        while l <= r:
            
            mid = (l+r)//2
            
            v1,v2 = isGood(mid)
            
            if v2:
                res = mid
                r = mid - 1
            
            if v1:
                l = mid + 1
            
            else:
                r = mid - 1
                
        
        return res % MOD
        