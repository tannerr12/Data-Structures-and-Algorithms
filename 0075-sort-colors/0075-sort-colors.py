class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l,r,j = 0,len(nums) -1,0

        
        while j <= r:
            
            if nums[j] == 0:
                nums[l],nums[j] = nums[j], nums[l]
                l+=1
                j+=1
            elif nums[j] == 2:    
                nums[r], nums[j] = nums[j], nums[r]
                r -= 1
            else:
                j += 1
        
        return nums
        