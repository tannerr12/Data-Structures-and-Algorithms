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
            
            #remove points where they all intersect
            al = mid // allLCM
            
            #sum up all of our results
            s = tarA + tarB + tarC - ab - ac - bc + al
            
            #are we above and = or below our target
            return s >= n 
            
        #check all lcms ahead of time
        abLCM = lcm(a,b)
        acLCM = lcm(a,c)
        bcLCM = lcm(b,c)
        allLCM = lcm(abLCM, c)
        
        #search range from 
        l,r = 0, 2 * 10**9
        
        while l < r:
            
            mid = l + (r-l)//2

            if isGood(mid):
                r = mid
            else:
                l = mid +1
                
        
        return l