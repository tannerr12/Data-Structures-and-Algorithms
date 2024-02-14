class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        odd = 0 
        even = 0
        
        for i in range(1, len(nums), 2):
            diff = 0
            if i > 0 and i < len(nums)-1:
                diff = max(0, nums[i] - nums[i-1] + 1, nums[i] - nums[i+1] + 1)
            elif i > 0:
                diff = max(0, nums[i] - nums[i-1] + 1)
            elif i < len(nums) -1:
                diff = max(0, nums[i] - nums[i+1] + 1)
            odd += diff
        
        
        for i in range(0, len(nums), 2):
            diff = 0
            if i > 0 and i < len(nums)-1:
                diff = max(0, nums[i] - nums[i-1] + 1, nums[i] - nums[i+1] + 1)
            elif i > 0:
                diff = max(0, nums[i] - nums[i-1] + 1)
            elif i < len(nums) -1:
                diff = max(0, nums[i] - nums[i+1] + 1)
            even += diff
    
        
        return min(odd,even)
            
                
                
        #123
        
        #2,1,3
        