class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        idx = 0
        end = len(nums) -1
        while idx < len(nums) and nums[idx] == 0:
            idx +=1
        
        while end >= 0 and nums[end] == 0:
            end -=1
            
        
        if idx > end:
            return 0
        elif idx == end:
            return 1
        
        groups = []
        idx +=1
        count = 0
        while idx <= end:
            
            if nums[idx] == 0:
                count +=1
            
            else:
                groups.append(count + 1)
                count = 0
            
            idx +=1
        
        
        res = 1
        for val in groups:
            res *= val
            res %= MOD
        
        return res % MOD
            
            
            