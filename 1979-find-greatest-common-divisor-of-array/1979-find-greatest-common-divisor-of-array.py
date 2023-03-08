class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        s = min(nums)
        m = max(nums)
        
        def gcd(x,y):
            
            while y:
                x,y = y, x % y
            
            return x
        
        return gcd(s,m)