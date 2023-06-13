class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nums.sort()
        
        left = nums[:math.ceil(len(nums) / 2)]
        right = nums[math.ceil(len(nums) / 2):]
        left.reverse()
        right.reverse()
        
        l,r = 0,0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = left[l]
                l+=1
            else:
                nums[i] = right[r]
                r +=1
        
        
            
            
        