class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        
        stack = []
        
        for i in range(len(nums)):
            
            while stack and stack[-1] > nums[i] and k - len(stack) < (len(nums) - i):
                
                stack.pop()
                
            
            stack.append(nums[i])
        
        
        
     #   if len(stack) < k:
     #       stack += nums[-k:]
        
        return stack[:k]