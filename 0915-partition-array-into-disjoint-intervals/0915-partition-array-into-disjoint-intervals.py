class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = float('-inf')
        mxRight = [0] * len(nums)
        mnRight = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            mnRight[i] = mn
            mxRight[i] = mx
            mx = max(mx,nums[i])
            mn = min(mn, nums[i])
        
        res = float('inf')
        mx = float('-inf')
        mn = float('inf')
        for i in range(len(nums) -1):
            mx = max(nums[i], mx)
            mn = min(nums[i], mn)
            if mx <= mnRight[i]:
                res = min(res, i+1)
            elif mn >= mxRight[i]:
                res = min(res, len(nums) - i - 1)
        
        return res
            
        