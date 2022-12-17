class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums  = [1] + nums + [1]
        
        @cache
        def dfs(i,j):
            
            if j - i < 0:
                return 0
            res = 0
            for k in range(i,j+1):
                res = max(res, nums[i - 1] * nums[k] * nums[j +1] + dfs(k+1,j) + dfs(i,k-1))
                
            
            if res == float('inf'):
                return 0
            
            return res
        
        
        
        return dfs(1,len(nums) -2)