class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        
        res = 0
        factor = set()
        i = 1
        while i * i <= a:
            
            if a % i == 0:
                factor.add(a//i)
                factor.add(i)
            i+=1
        
        i =1
        while i * i <= b:
            
            if b % i == 0:
                if i in factor:
                    res +=1
                
                if b // i != i and b//i in factor:
                    res +=1
            i +=1
        
        return res
        