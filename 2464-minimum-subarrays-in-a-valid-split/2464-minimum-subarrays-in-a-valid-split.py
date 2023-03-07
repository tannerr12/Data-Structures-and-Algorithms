class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i,j):
            
            if j == len(nums) -1 and gcd(nums[i],nums[j]) > 1:
                return 1
            elif j == len(nums)-1:
                return float('inf')
            
            res = float('inf')
            #check gcd and if true go down that path if not skip it
            if gcd(nums[i], nums[j]) > 1:
                res = min(res,dfs(j+1,j+1) + 1)
            
            res = min(res, dfs(i, j+1))

            return res
        
        
        res = dfs(0,0)
        
        return res if res != float('inf') else -1
        
        