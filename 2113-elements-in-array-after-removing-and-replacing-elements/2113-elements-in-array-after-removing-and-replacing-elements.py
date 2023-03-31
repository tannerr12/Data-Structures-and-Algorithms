class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        
        for i in range(len(queries)):
            
            queries[i].append(i)
            
            
        queries.sort()
        
        idx = 0
        time = 0
        turn = False
        
        
        res = [-1] * len(queries)
        for t,j,i in queries:
            
            idx = t % len(nums)
            cycle = t // len(nums)
            if cycle % 2 == 1 and idx == 0:
                continue
            elif cycle % 2 == 0 and j + idx < len(nums):
                ans = nums[j + idx]
                res[i] = ans
            elif cycle % 2 == 1 and j < idx:
                ans = nums[j]
                res[i] = ans

        return res
                
        