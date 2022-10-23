class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        l,r = 0, len(nums) -1
        
        
        while l <= r:
            
            
            
            curr = (l+r) // 2
            
            
            calc = len(nums) - curr
            
            
            
            
            if nums[curr] >= calc:
                if curr == 0 or nums[curr -1] < calc:
                    return calc
                else:
                     r = curr  - 1
            
            
            else:
                l = curr + 1

        return -1