class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        count = 0
        offset = 0
        prev = nums[0]
        for i in range(len(nums)):
            
            if i > 0 and nums[i] != prev:
                count = 0
            count +=1
            
            if count > 2:
                prev = nums[i]
                nums[i] = None
                offset +=1
            
            else:
                prev = nums[i]
                nums[i - offset] = nums[i]
              
            
            
        
        
        print(nums)
        return len(nums) - offset