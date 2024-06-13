class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            
            res = float('-inf')
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    res = max(res, dfs(j) + 1)
            
            
            return res
        
        
        ans = dfs(0)
        
        return ans if ans != float('-inf') else -1
    
        
            
            