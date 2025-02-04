class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        best = nums[0]
        cur = nums[0]
        

        for i in range(1, len(nums)):
            num = nums[i]
            if num > nums[i-1]:
                cur += num
            
            else:
                cur = num
            best = max(best, cur)
        
        return best
            
