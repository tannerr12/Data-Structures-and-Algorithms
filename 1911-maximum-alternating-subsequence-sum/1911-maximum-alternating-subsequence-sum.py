class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        #nums = [1] * (10 ** 5)
        @cache
        def dfs(i, count):
            
            if i >= len(nums):
                return 0
            
            res = 0
            if count:
                res = max(res,dfs(i+1,not count) - nums[i])
            else:
                res = max(res,dfs(i+1,True) + nums[i]) 
            
            
            res = max(res,dfs(i+1, count))
            
            return res
        
        return dfs(0,False)
        
        
            
            