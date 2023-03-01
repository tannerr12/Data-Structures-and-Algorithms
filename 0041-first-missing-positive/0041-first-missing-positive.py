class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        s = set(nums)
        
        for i in range(1,(10**5) + 2):
            if i not in s:
                return i
        
        return 0