class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i, cur):
            
            if i >= len(nums):
                return 0
            
            res = float('inf')
            #remove
            res = min(res, dfs(i+1, cur) + 1)
            
            if nums[i] >= cur:
                #keep
                res = min(res, dfs(i+1, nums[i]))
            
            
            return res
        
        return dfs(0,1)