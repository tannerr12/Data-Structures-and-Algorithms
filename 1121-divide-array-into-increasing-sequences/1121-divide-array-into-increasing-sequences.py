class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        sequences = max(c.values())
        return len(nums) / sequences >= k
        