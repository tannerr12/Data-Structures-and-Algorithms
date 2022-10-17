class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        
        
        l,r = 0,len(nums) -1
        
        
        
        while l <= r:
            
            curr = (l+r) // 2
            
            
            if nums[curr] == target:
                #gather pointers
                x,y = curr,curr
                
                while x < len(nums)-1 and nums[x+1] == target:
                    x+=1
                
                while y > 0 and nums[y-1] == target:
                    y-=1
                
                return[y,x]
            
            
            elif nums[curr] > target:
                r = curr -1
                
            else:
                l = curr + 1
                
        
        
        return [-1,-1]
    