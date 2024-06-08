class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        
        
        arr = [0 for j in range(len(nums))]
        
        small = nums[0]
        large = nums[-1]
        
     
        for i in range(len(nums)-1,0,-1):
            arr[i] = large
            large = min(large, nums[i])
        
        
        res = 0
        for i in range(1, len(arr)-1):
            if nums[i] > small and nums[i] < arr[i]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
            
            small = max(small, nums[i])
        return res
        