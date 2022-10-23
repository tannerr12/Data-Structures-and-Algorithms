class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        doubled = -1
        missing = -1
        
        if nums[0] > 1:
            missing = 1
        
        for i in range(1,len(nums)):
            
            if nums[i-1] == nums[i]:
                doubled = nums[i]
                
                
            
            elif nums[i-1] != nums[i] -1:
                missing = nums[i] -1
                
            
        
        if missing == -1:
            missing = len(nums)
        return [doubled,missing]
                
            
        
        