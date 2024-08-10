class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i):
            
            if i >= len(nums) -1:
                return 0
            
            res = float('-inf')
            
            for j in range(i+1, len(nums)):
                res = max(res, dfs(j) + ((j - i) * nums[j]))
            
            
            return res
        
        
        return dfs(0)
                