class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
            
            l = 0
            r = len(nums) -1
            if nums[0] == target:
                return True
            
            while l < r:
                
                curr = (l + r) // 2

                if nums[curr] < nums[r]:
                    r = curr
                
                elif nums[curr] > nums[r]:
                    
                    l = curr +1
                else:
                    while l < r and nums[r-1] == nums[r]:
                        r -=1
                    while l< r and nums[l +1] == nums[l]:
                        l+=1
                

     
            pivot = l
            l = 0
            r = len(nums) -1
      
            
            while l <= r:
                
                curr = (l + r) // 2
                curr2  = (curr + pivot) % len(nums)

                if nums[curr2] == target:
                    return True
                
                elif target < nums[curr2]:
                    r = curr - 1
                
                else:
                    l = curr + 1
            
            
            
            
            return False
        
        
