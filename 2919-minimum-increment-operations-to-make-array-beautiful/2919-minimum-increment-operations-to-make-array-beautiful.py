class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        @cache
        def dfs(i,d):
   
            if i >= len(nums):
                return 0
            
            res = float('inf')    
            #skip
            if d > 0:
                res = min(res, dfs(i+1, d - 1))
            #top up
            res = min(res, dfs(i+1, 2) + max(0, k - nums[i]))
            
            
            return res
        
        
        return dfs(0, 2)
        