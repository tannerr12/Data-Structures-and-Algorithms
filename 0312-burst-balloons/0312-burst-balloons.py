class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """ 
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
        """
        
       
        
        
        
        nums = [1] + nums + [1]
        n = len(nums)
        dp= [[0 for j in range(len(nums))] for i in range(len(nums))]   
        for left in range(n - 2, -1,-1):
            for right in range(left + 2, n):
                
                for k in range(left+1,right):
                    dp[left][right] = max(dp[left][right], dp[left][k] + dp[k][right] + (nums[left] * nums[k] * nums[right]))
                
        
        print(dp)
        return dp[0][-1]