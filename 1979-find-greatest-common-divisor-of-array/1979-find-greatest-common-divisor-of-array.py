class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        s = min(nums)
        m = max(nums)
        
        return gcd(s,m)