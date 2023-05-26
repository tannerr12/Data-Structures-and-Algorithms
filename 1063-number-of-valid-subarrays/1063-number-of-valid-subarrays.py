class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        
        stack = []
        res = 0
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                res += i - idx
            
            
            stack.append(i)
        
        
        while stack:
            idx = stack.pop()
            res += len(nums) - idx
        
        return res
            