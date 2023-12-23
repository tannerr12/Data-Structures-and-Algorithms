class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        l = 0 
        res = 0
        count = 0
        target = max(nums)
        for i in range(len(nums)):
            
            if nums[i] == target:
                count += 1
                
            
            while count >= k:
                res += len(nums) - i
                if nums[l] == target:
                    count -= 1
                l += 1
        
        return res
            