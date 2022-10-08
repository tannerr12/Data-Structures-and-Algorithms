class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i, nums, target):
            

            if target == 0 and len(nums) == k:
                res.append(nums.copy())
                return
            if i > 9:
                return
            nums.append(i)
            dfs(i+1,nums,target - i)
            nums.pop()
            
            dfs(i+1, nums,target)
            
            return
        
        
        dfs(1,[],n)
        
        return res