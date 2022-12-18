class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        stack, n = [], len(nums)
        
        ans = [0] * n
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] >= num:
                min_idx = stack.pop()
                left,right = (stack[-1] + 1) if stack else 0, i
                window = right - left -1
                ans[window] = max(ans[window], nums[min_idx])
            stack.append(i)
            
        
        else:
            while stack:
                min_idx = stack.pop()
                left,right = (stack[-1] + 1) if stack else 0, n
                window = right - left -1
                ans[window] = max(ans[window], nums[min_idx])
        
        
        for i in range(n-2, -1,-1):
            ans[i] = max(ans[i], ans[i+1])
            
        
        return ans
    
            
        