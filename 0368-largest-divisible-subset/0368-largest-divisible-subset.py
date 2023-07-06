class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        path = []
        p = []
        
        @cache
        def dfs(i):
            
            tail = nums[i]
            maxSubset = []
            
            for p in range(0, i):
                if tail % nums[p] == 0:
                    subset = dfs(p)
                    if len(maxSubset) < len(subset):
                        maxSubset = subset
            
            maxSubset = maxSubset.copy()
            maxSubset.append(tail)
            
            return maxSubset
        
        return max([dfs(i) for i in range(len(nums))], key = len)