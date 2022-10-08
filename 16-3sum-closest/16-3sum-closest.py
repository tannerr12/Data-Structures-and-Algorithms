class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        res = float('inf')
        nums.sort()
        for i in range(len(nums)):
            
            l,r = i+1, len(nums) -1
            n = nums[i]
            
            while l < r:
                
                val = nums[l] + nums[r] + n
                ttar = target - n
                if val > target:
                    r -=1
                elif val < target:
                    l+=1
                else:
                    return target
                
                tdiff = abs(target - (val)) 
                if tdiff < diff:
                    diff = tdiff
                    res = val
                
        return res
                    
        