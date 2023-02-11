class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        for i in range(len(nums)):
            
            m = i
            
            for j in range(i+1, len(nums)):
                
                if nums[j] < nums[m]:
                    m = j
            
            
            nums[m],nums[i] = nums[i], nums[m]
            
            
            
        