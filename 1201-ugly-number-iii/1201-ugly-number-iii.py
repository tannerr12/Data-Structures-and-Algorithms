class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        def lcm(a,b):
            
            return a * b // gcd(a,b)
        
        def isGood(mid):
            
            #calculate how many solves are before this number for each a, b and c
            
            tarA = mid // a
            tarB = mid // b
            tarC = mid // c
            
            
            
            #remove intersection points
            ab = mid // abLCM
            ac = mid // acLCM
            bc = mid // bcLCM
            
            al = mid // allLCM
            
            s = tarA + tarB + tarC - ab - ac - bc + al
            
            return s >= n 
            
        abLCM = lcm(a,b)
        acLCM = lcm(a,c)
        bcLCM = lcm(b,c)
        allLCM = lcm(abLCM, c)
        l,r = 0, 10**18
        
        while l < r:
            
            mid = (l+r)//2
            
            val = isGood(mid)
            
            if val:
                r = mid
            else:
                l = mid +1
                
        
        return l