class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        bit = 0
        for i in range(1, len(nums) -1):
            if i % 3 == 0:
                bit ^= 1
                
            if i % 2:
                nums[i], nums[i+1] = nums[i+1],nums[i]
        