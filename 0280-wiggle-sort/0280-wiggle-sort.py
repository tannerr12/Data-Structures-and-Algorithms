class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        #print(nums)
        alter = 0
        for i in range(1, len(nums) -1):
            
            if i % 3 == 0:
                alter ^= 1
            if (alter == 1 and i % 2 == 1) or (alter == 0 and i % 2) and i % 3:
                nums[i], nums[i+1] = nums[i+1],nums[i]
        

            
        return nums