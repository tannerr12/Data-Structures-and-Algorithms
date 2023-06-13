class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        
        dpMn = [0] * len(nums)
        
        mx = float('-inf')
        
        for i in range(len(nums)):
            
            dpMn[i] = mx
            mx = max(mx, nums[i])
        
        
        res = 0
        mn = float('inf')
        for i in range(len(nums)-1,-1,-1):
            
            if nums[i] > dpMn[i] and nums[i] < mn:
                res +=1 
            
            
            mn = min(nums[i],mn)
            
        
        return res
            
            