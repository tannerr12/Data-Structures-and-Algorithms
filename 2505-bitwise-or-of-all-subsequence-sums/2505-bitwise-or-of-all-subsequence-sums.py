class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        
        num = 0
        total = 0
        for val in nums:
            total += val
            
            num |= val
            num |= total
            
        return num
            