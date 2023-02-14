class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = float(-inf)
        curr = 0
        for num in nums:
            if curr + num > num:
                curr += num
            else:
                curr = num
            
            m = max(m,curr)
        
        
        return m