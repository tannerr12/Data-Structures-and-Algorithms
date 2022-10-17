class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        #left
        
        l,r = 0,len(nums) -1
        
        left,right = -1,-1
        
        while l <= r:
            
            curr = (l+r) // 2
            
            
            
            if nums[curr] > target:
                r = curr -1
                
            elif nums[curr] < target:
                l = curr + 1
            else:
                left = curr
                r = curr -1
                
        
        l,r = 0,len(nums) -1
        
        
        
        while l <= r:
            
            curr = (l+r) // 2
            
            
            
            if nums[curr] > target:
                r = curr -1
                
            elif nums[curr] < target:
                l = curr + 1
            else:
                right = curr
                l = curr +1
                        
        
        
        
        
        #right
        
        
        return [left,right]
    