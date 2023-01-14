class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        
        val = 0
        
        for i in range(len(nums)):
            val |= nums[i]
            
        return val
            