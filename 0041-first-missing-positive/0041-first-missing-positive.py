class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #we will do 3 loops the first one will set all of the negative values to 0 as a not used option
        #the second will flip all of the values indexs we have seen to negative to mark them but not remove the values
        #We set any 0s we see to negative inf as to not mess up the positive process since inf cannot be found in the list
        #finally we return the first non negative number we find or if we do not find one we can return the len of the list + 1 since that would be the worst case
        for i in range(len(nums)):
            
            if nums[i] < 0:
                nums[i] = 0
        
        
        for i in range(len(nums)):
            val = abs(nums[i])
            
            if val -1 < len(nums) and val -1 >= 0:
                
                if nums[val-1] == 0:
                    nums[val-1] = float('-inf')
                else:
                    if nums[val-1] > 0:
                        nums[val-1] = -1* nums[val-1]
        
        print(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        
        return len(nums) +1