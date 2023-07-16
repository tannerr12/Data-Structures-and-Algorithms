class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        n = len(nums) // 2
        pairs = list(zip(nums[:n], list(reversed(nums))[:n]))
        mins = sorted(map(min, pairs))
        maxs = sorted(map(max, pairs))
        sums = collections.Counter(map(sum, pairs))
        
        ans = 1e9
        for t in range(2, 2 * limit + 1):
            already_equal = sums[t]
            increase_both = bisect.bisect_left(maxs, t - limit)
            decrease_both = n - bisect.bisect_left(mins, t)
            ans = min(ans, n - already_equal + increase_both + decrease_both)

        return ans