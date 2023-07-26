class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        stack = []
        for i in range(len(nums)-1,-1,-1):
            
            if stack and stack[-1] >= nums[i]:
                val = stack.pop()
                stack.append(val + nums[i])
            
            else:
                stack.append(nums[i])
        
        return max(stack)