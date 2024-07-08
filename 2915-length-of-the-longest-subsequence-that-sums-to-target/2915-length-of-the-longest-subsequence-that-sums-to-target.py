class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        @lru_cache(None)
        def dfs(i,total):
            if total == target:
                return 0 

            if i >= n or total > target:
                return float("-inf")

            return max(dfs(i+1,total),1+dfs(i+1,total+nums[i]))

        val = dfs(0,0)
        dfs.cache_clear()
        return val if val != float("-inf") else -1