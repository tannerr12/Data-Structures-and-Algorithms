class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
        arr = []
        res = float('inf')
        for i in range(x,len(nums)):

            insort(arr, nums[i-x])
            idx = bisect_left(arr, nums[i])
            
            if idx < len(arr):
                diff = min(abs(nums[i] - arr[idx]), abs(nums[i] - arr[idx-1]))
            else:
                diff = abs(nums[i] - arr[idx-1])
            res = min(res, diff)
            
        
        return res