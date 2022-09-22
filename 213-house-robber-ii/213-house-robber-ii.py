class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
   
        def rob(i,total,memo,nums):

            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            
            high = max(rob(i+1,total,memo,nums), rob(i+2,total,memo,nums) + nums[i])
            memo[i] = high
            
            return high
        
        
        
        return max(rob(0,0,{},nums[1:]), rob(0,0,{},nums[:-1]))