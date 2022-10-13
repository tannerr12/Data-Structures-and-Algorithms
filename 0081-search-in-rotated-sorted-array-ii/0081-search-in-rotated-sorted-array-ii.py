class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
       
        return target in nums
        
        def binSearch():
            minL = nums[0]
            maxL = nums[0]
            maxr = nums[-1]
            minr = nums[-1]
            l = 0
            r = len(nums) -1
            pivot = -1
            
            while l < r:
                
                curr = (l + r) // 2
                
                if nums[curr -1] > nums[curr] or (curr != len(nums) -1 and nums[curr + 1] < nums[curr]) or (nums[0] < nums[curr]):
                    pivot = curr
                    minr = nums[curr+1] if curr < len(nums)-1 else nums[0]
                    maxl = nums[curr-1]
                    
                
                if nums[curr] == target:
                    return True
                
                elif target < minL:
                    r = curr + 1
                
                elif target > minL:
                    l = curr - 1
            
            
            return False
        
        
        return binSearch()