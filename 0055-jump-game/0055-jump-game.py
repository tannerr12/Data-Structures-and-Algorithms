class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #start at the end and go backwards
        
        goal = len(nums) -1
        
        
        for i in range(len(nums) -1, -1,-1):
            
            if i + nums[i] >= goal:
                goal = i
            
            
        
        
        return True if goal == 0 else False 