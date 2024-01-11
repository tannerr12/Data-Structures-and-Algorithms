class Solution:
    def minimumAddedCoins(self, nums: List[int], target: int) -> int:
        nums.sort()
        current_max = 0
        additions = 0
        index = 0

        while current_max < target:
            if index < len(nums) and nums[index] <= current_max + 1:
                current_max += nums[index]
                index += 1
            else:
                current_max += current_max + 1
                additions += 1

        return additions