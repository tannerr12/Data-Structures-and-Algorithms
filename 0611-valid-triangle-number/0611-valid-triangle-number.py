class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                
                a = nums[i]
                b = nums[j]
                target = a + b - 1
                
                idx = bisect_right(nums, target)
                if idx >= len(nums) or nums[idx] > target:
                    idx -=1
                
                res += max(0,idx - j)
                
        
        return res
                
                