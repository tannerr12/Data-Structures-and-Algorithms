class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        count = [0] * (max(nums) +1)
        
        for val in nums:
            count[val] +=1
        
        
        
        idx = 0
        
        for i,val in enumerate(count):
            
            count[i] = idx
            
            idx += val
        
        print(count)
        ncopy = [0] * len(nums)
        for i,val in enumerate(nums):
            ncopy[count[val]] = val
            count[val] +=1
        
        
        for i,v in enumerate(ncopy):
            nums[i] = ncopy[i]
            
            
            
        