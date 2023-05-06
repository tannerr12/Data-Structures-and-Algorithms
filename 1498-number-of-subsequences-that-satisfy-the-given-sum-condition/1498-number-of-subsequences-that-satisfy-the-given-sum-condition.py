class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        MOD = 10 ** 9 + 7
        res = 0
        for i in range(len(nums)):
            
            if nums[i] * 2 <= target:
                
                r = bisect_right(nums, target - nums[i])
                if r >= len(nums) or nums[r] > target - nums[i]:
                    r -=1
                res += (2 ** (r - i)) % MOD
                res %= MOD 
        
        
        return res
                