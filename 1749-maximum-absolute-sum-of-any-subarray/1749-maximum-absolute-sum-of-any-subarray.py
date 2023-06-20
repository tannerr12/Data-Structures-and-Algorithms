class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res = 0
        resm = 0
        tmax = 0
        tmin = 0
        for i in range(len(nums)):
            tmin = min(nums[i], tmin + nums[i])
            tmax = max(nums[i], tmax + nums[i])
            
            res = max(res, tmax)
            resm = min(resm, tmin)
        
        
        return max(abs(resm), res)
            
        