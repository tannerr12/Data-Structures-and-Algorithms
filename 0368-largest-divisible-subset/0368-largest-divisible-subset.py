class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        return list(max(subsets.values(), key=len))
    
    
        nums.sort()
        
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