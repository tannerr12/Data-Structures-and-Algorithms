class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        

        arr = []
        res = 0
        
        for i in range(len(nums)):
            
            if not arr or arr[-1][0] < nums[i]:
                arr.append([nums[i],i])
                
            
            idx = bisect_right(arr, nums[i], key= lambda x: x[0])
            
            if idx < len(arr):
                res = max(res, i - arr[idx][1] + 1)
        
        return res if res > 1 else 0