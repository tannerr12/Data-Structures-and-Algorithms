class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        def lcm(x,y):
            
            return x * y // gcd(x,y)
        
        return lcm(2,n)