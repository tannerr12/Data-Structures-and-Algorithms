class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        
        @cache
        def dfs(i, k):

            if i >= len(nums):
                return 0
            if k == -1:
                return float('inf')
            
            ans = float('inf')
            mx = nums[i]
            total = 0
            
            for j in range(i, len(nums)):
                
                mx = max(mx, nums[j])
                total += nums[j]
                wasted = ((j - i + 1) * mx) - total
                ans = min(ans, dfs(j+1, k-1) + wasted)
            
            return ans
        
        
        return dfs(0,k)
                
        
        
                
        