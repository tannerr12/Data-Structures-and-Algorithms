class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        
        
        arr = [[0,0] for j in range(len(nums))]
        
        small = nums[0]
        large = nums[-1]
        
        for i in range(1, len(nums) -1):
            arr[i][0] = small
            small = max(small, nums[i])
        
        for i in range(len(nums)-1,0,-1):
            arr[i][1] = large
            large = min(large, nums[i])
        
        
        res = 0
        for i in range(1, len(arr)-1):
            if nums[i] > arr[i][0] and nums[i] < arr[i][1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
        
        return res
        