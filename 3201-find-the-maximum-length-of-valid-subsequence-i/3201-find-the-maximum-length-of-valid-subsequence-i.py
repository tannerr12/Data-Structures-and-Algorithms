class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        #2 groups
        #odd + odd 
        #even + even
        
        #odd + even
        #even + odd
        
        @cache
        def dfs(i,curr):
            
            if i >= len(nums):
                return 0
            
            ans = float('-inf')
            if (curr == 0 and nums[i] % 2) or (curr == 1 and nums[i] % 2 == 0):
                ans = max(ans, dfs(i + 1, curr))
            
            else:
                ans = max(ans, dfs(i + 1, curr))
                ans = max(ans, dfs(i + 1, nums[i] % 2) + 1)
                
                
            
            
            return ans
            
        @cache
        def dfs2(i,curr):
            
            if i >= len(nums):
                return 0
            
            ans = float('-inf')
            if (curr == 0 and nums[i] % 2 == 0) or (curr == 1 and nums[i] % 2):
                ans = max(ans, dfs2(i + 1, curr))
            
            else:
                ans = max(ans, dfs2(i + 1, curr))
                ans = max(ans, dfs2(i + 1, nums[i] % 2) + 1)
                
                
            
            
            return ans
                
                
            
            
        
        return max(dfs(0, -1), dfs2(0, -1))
        
        