class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        
        s = sum(nums)
        
        nums.sort()
        median = nums[len(nums) // 2]
       
        
        
        res = 0
        
        for i in range(len(nums)):
            
            res += abs(median - nums[i])
            
            
        
        
        return res