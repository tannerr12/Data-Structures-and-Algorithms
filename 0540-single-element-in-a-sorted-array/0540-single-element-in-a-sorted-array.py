class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        l,r = 1, (len(nums) -2) 
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        
        while l <= r:
            
            
            curr = (l+r) // 2
            
            rem = curr % 2
            
            if nums[curr] != nums[curr -1] and nums[curr] != nums[curr +1]:
                return nums[curr]
            
            elif (rem and nums[curr] == nums[curr -1]) or (rem == 0 and nums[curr] == nums[curr +1]):
                l = curr +1
            
            else:
                r = curr -1
                
        
        
        return -1