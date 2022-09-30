class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        
        if len(nums) < 3:
            return 0
        
        dp = collections.defaultdict(int)
        def dfs(i):
            
            if i >= len(nums):
                return

            if nums[i] - nums[i-1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0
            
            
            dfs(i+1)

                
           
                
        
        #for i in range(len(nums)):
        dfs(2)
        
        #print(dp)
        
        return sum(dp.values())
        