class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        target = len(nums) //2 
        
        @cache
        def dfs(i,bitmask):
            nonlocal target
            if i > target:
                return 0
            
            res = 0
            for k in range(len(nums)):
                if (1 << k) & bitmask > 0:
                    continue
                for j in range(len(nums)):
                    if j == k:
                        continue
                    if (1 << j) & bitmask > 0:
                        continue
                    
                    res = max(res, dfs(i+1,bitmask | (1 << k) | (1 << j)) + i * gcd(nums[k], nums[j]))
         
            
            
            return res
        
        
        return dfs(1, 0)
        
        