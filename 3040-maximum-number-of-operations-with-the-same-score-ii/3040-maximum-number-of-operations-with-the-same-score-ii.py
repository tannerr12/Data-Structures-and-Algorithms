class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        #only 3 number choices to attempt
        
        one = nums[0] + nums[1]
        two = nums[-1] + nums[-2]
        three = nums[0] + nums[-1]
        
        trys = []
        trys.append(one)
        trys.append(two)
        trys.append(three)
        
        @cache
        def dfs(l,r,target):
            
            if l >= r:
                return 0
            
            res = 0
            if nums[l] + nums[r] == target:
                res = max(res, dfs(l+1,r-1,target) + 1)
            if nums[l] + nums[l+1] == target:
                res = max(res, dfs(l+2,r,target) + 1)
            if nums[r] + nums[r-1] == target:
                res = max(res, dfs(l,r-2,target) + 1)
            
            return res
            
        ans = 0
        for val in trys:
            ans = max(ans, dfs(0, len(nums) - 1, val))
        
        return ans