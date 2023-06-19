class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        mx = 0
        
        for val in gain:
            res += val
            mx = max(mx,res)
        
        return mx