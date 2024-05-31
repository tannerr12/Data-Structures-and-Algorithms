class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = float('-inf')
        vals = defaultdict(int)
        
        prefix = []
        prefix.append(0)
        
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        for i in range(len(nums)):
            
            if nums[i] + k in vals:
                res = max(res, prefix[i+1] - prefix[vals[nums[i] + k]])
            if nums[i] - k in vals:
                res = max(res, prefix[i+1] - prefix[vals[nums[i] - k]])
            
            vals[nums[i]] = i if (nums[i] not in vals or prefix[i] - prefix[vals[nums[i]]] <= 0) else vals[nums[i]]
        
        return res if res != float('-inf') else 0