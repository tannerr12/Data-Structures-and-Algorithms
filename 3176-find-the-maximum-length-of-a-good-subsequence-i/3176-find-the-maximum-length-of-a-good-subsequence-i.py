class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        
        @cache
        def dfs(i,k):
            
            res = 0
            
            for j in range(i+1, len(nums)):
                if i == -1 or nums[j] == nums[i]:
                    res = max(res, dfs(j,k) + 1)
                elif k > 0:
                    res = max(res, dfs(j,k-1) + 1)
                
                
            return res
        
        
        return dfs(-1, k)
            
            