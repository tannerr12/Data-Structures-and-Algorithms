class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
 
        used = False
        nums = nums
        for i in range(1, len(nums)):
            
            if nums[i] < nums[i-1] and not used:
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]     
                used = True
            elif nums[i] < nums[i-1] and used:
                return False
        
        return True
                