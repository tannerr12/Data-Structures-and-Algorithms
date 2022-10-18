class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        l,r = 0 , len(nums) -1
        
        while l <= r:
            
            
            curr = (l+r) //2
            
            if curr == len(nums) -1 and nums[curr -1] < nums[curr]:
                return curr
            
            elif curr == 0 and nums[curr + 1] < nums[curr]:
                return curr
                
            
            elif (curr != 0 and nums[curr -1] < nums[curr]) and (curr != len(nums) and nums[curr + 1] < nums[curr]):
                return curr
            
            elif (curr != 0 and nums[curr -1] > nums[curr]):
                r = curr -1
                
            elif (curr!= len(nums) -1 and nums[curr + 1] > nums[curr]):
                l = curr +1
            
            else:
                r = curr -1
            
        
        
        return l