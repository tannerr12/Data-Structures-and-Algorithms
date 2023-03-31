class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        

        idx = 0
            
        res = [-1] * len(queries)
        i = 0
        for t,j in queries:
            
            idx = t % len(nums)
            cycle = t // len(nums)
            if cycle % 2 == 1 and idx == 0:
                i+=1
                continue
            elif cycle % 2 == 0 and j + idx < len(nums):
                ans = nums[j + idx]
                res[i] =ans
            elif cycle % 2 == 1 and j < idx:
                ans = nums[j]
                res[i] =ans
            
            
            i+=1
        return res
                
        