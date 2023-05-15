class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        
        for i in range(len(nums)):
            x = nums[i]
            nums[i] = a * x ** 2 + b * x + c
        
        nums.sort()
        return nums