class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        stack = []
        right = [len(nums)-1] * len(nums)

        stack = []
        for i in range(len(nums)-1,-1,-1):
            
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
                
            if stack:
                right[i] = stack[-1] -1 
                
            stack.append(i)
        
        
        res = 0
        stack = []
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
                
            val = 0   
            if stack:
                val = stack[-1] + 1 
                
            stack.append(i)
            if val <= k and right[i] >= k:
                res = max(res, nums[i] * (right[i] - val +1))
        
        return res