class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        mx = max(c.values())
        
        sm = sum(s for k,s in c.items() if s == mx)
        
        return sm