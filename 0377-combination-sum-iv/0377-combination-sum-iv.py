class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
     
        
        
        memo = {}
        
        
        
        
        @lru_cache(maxsize = None)
        def dfs(i,remain):

            if remain == 0:
                return 1
            
            if (i,remain) in memo:
                return memo[(i,remain)]
            
            result = 0
            for i in range(len(nums)):
      
                if nums[i] <= remain:
                    
                    result += dfs(i,remain - nums[i])
            
            
            
            memo[(i,remain)] = result
            return result
            
        
        return dfs(0,target)
            