class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        #print(nums)
        res =0
        for i in range(len(nums)-1, len(nums)//2 -1,-1):
            if nums[i] < k:
                res += k - nums[i]
        
        for i in range(len(nums)//2 + 1):
            if nums[i] > k:
                res += nums[i] - k
        return res
        