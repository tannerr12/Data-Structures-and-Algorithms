class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        org = len(nums)
        total = sum(nums)
        cycles = target // total
        target -= total * cycles
        nums = nums + nums
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
        res = float('inf')
        for i in range(len(nums) // 2):
            t = prefix[i] + target
            idx = bisect_left(prefix, t)
            
            if idx < len(prefix) and prefix[idx] == t:
                res = min(res, idx - i)
        
        return res + (org * cycles) if res != float('inf') else -1
            