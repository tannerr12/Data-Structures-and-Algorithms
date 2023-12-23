class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        l = 0 
        res = 0
        target = max(nums)
        for i in range(len(nums)):
            
            if nums[i] == target:
                k -= 1
                
            
            while k == 0:
                res += len(nums) - i
                if nums[l] == target:
                    k += 1
                l += 1
        
        return res
            