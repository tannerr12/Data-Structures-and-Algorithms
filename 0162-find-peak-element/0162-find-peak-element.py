class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        l,r = 0 , len(nums) -1
        
        while l < r:
            
            
            curr = (l+r) //2
            
            
            if nums[curr] > nums[curr +1]:
                r = curr 
            
            else:
                l = curr +1
            
        
        
        return l