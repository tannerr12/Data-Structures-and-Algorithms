class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 3:
            return 0
        
        nums.sort()
        res = float('inf')
        
        for i in range(len(nums)):
        
            
            #take 3 from left
            if i >= 3:
                res = min(res, abs(nums[3] - nums[-1]))
            if i < len(nums) - 4:
                res = min(res, abs(nums[0] - nums[-4]))
            
            if i >= 2 and i < len(nums) - 2:
                res = min(res, abs(nums[2] - nums[-2]))
            
            if i >= 1 and i < len(nums) - 3:
                res = min(res, abs(nums[1] - nums[-3]))

        return res