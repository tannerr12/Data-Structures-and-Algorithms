class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        if nums[0] > 0:
            res += 1
            
        for i in range(len(nums)):
            
            if i + 1 > nums[i]:
                if i == len(nums) -1 or nums[i+1] > i + 1:
                    res += 1
        
        return res
            
        