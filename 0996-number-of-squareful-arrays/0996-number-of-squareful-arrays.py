class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        res = []
        
        def dfs(nums,cur_path):
            if not nums:
                res.append(list(cur_path))
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                
                if cur_path and not isSquare(cur_path[-1] + nums[i]):
                    continue
                
                cur_path.append(nums[i])
                dfs(nums[:i] + nums[i+1:], cur_path)
                cur_path.pop()
        
        def isSquare(num):
            return pow(isqrt(num), 2) == num
        
        
        nums.sort()
        dfs(nums, [])
        return len(res)
            