class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #first find the minimum and maximum numbers
        l = len(nums)
        nums = list(set(nums))
        nums.sort()
        
        #1,2,3,5,6
        
        #1 -> 5 right of 5 + left of 1 = 1
        #2 -> 6 right of 6 + left of 2 = 1
        #3 -> 7 right of 7 + left of 3 = 2
        
        #1,1,1,2,3,5,6
        
        res = float('inf')
        for i in range(len(nums)):
            
            idx = bisect_right(nums, nums[i] + l -1)
            res = min(res, len(nums) - idx + i)
            
        
        return res + l - len(nums)
        