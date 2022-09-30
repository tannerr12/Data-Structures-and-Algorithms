class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        
        if len(nums) < 3:
            return 0
        
        #dp = collections.defaultdict(int)
        s = 0
        def dfs(i,prev):
            nonlocal s
            if i >= len(nums):
                return

            if nums[i] - nums[i-1] == nums[i - 1] - nums[i - 2]:
                prev = prev + 1
                s += prev
            else:
                prev = 0
                
            
            
            dfs(i+1,prev)

                
           
                
        
        #for i in range(len(nums)):
        dfs(2,0)
        
        
        
        return s
        