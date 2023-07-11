class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        l = 0
        h = defaultdict(int)
        h[0] = 1
        total = 0
        res = 0
        for i in range(len(nums)):
            total += nums[i]
            
            res += h[total - k]
            h[total] += 1
        
        return res
            
            
            
        