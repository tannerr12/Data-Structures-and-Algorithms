class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        
        
        dist = len(nums)
        while dist > 1:
            
           
            for i in range(dist -1): 
                nums[i] = (nums[i] + nums[i+1]) % 10
            
            dist -=1
        
        
        return nums[0]
            