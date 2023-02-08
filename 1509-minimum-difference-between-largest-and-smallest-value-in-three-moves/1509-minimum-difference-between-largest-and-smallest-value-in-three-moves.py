class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        res = float('inf')
        
        #take 3 from left
        res = min(res, abs(nums[3] - nums[-1]))
        res = min(res, abs(nums[0] - nums[-4]))
        res = min(res, abs(nums[2] - nums[-2]))
        res = min(res, abs(nums[1] - nums[-3]))

        return res