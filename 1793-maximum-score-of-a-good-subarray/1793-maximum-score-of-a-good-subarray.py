class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        stack = []
        left = [0] * len(nums)
        right = [len(nums)-1] * len(nums)
        for i in range(len(nums)):
        
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
                
            if stack:
                left[i] = stack[-1] + 1 
                
            stack.append(i)
        
        
        stack = []
        for i in range(len(nums)-1,-1,-1):
            
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
                
            if stack:
                right[i] = stack[-1] -1 
                
            stack.append(i)
        
        
        res = 0
        for i in range(len(nums)):
            
            if left[i] <= k and right[i] >= k:
                res = max(res, nums[i] * (right[i] - left[i] +1))
        
        return res