class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos = 0
        
        for i in range(len(nums)):
            
            while pos < len(nums) and nums[pos] & 1 == 0:
                pos += 1
                
            if i > pos and (nums[i] & 1 == 0):
                nums[pos],nums[i] = nums[i], nums[pos]
        
        return nums