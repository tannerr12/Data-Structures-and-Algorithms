class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        
        res = float('inf')
        #take 3 from left
        res = min(res, abs(nums[3] - nums[-1]))
        #take 3 from the right
        res = min(res, abs(nums[0] - nums[-4]))
        #take 2 from the left 1 from the right
        res = min(res, abs(nums[2] - nums[-2]))
        #take 2 from the right 1 from the left
        res = min(res, abs(nums[1] - nums[-3]))

        return res