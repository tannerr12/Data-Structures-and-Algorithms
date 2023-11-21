class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        #rev(nums[i]) - nums[i] == rev(nums[j]) - nums[j]
        
        MOD = (10 ** 9) + 7
        
        
        h = {}
        #total = 0
        res = 0
        
        for i in range(len(nums)):
            rev = int(str(nums[i])[::-1])
            if rev - nums[i] in h:
                res += h[rev-nums[i]]
                h[rev-nums[i]]+=1
            else:
                h[rev-nums[i]] = 1
                
        
        
        return res % MOD       
            