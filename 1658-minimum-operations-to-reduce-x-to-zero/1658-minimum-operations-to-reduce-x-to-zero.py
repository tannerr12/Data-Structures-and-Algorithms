class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #sum - x
        
        l = 0
        
        target = sum(nums) - x
        
        curr = 0
        res = -1
        for i in range(len(nums)):
            
            curr += nums[i]
            
            
            while l <= i and curr > target:
                
                curr -= nums[l]
                l+=1
                
            
            if curr == target:
                res = max(res, i - l + 1) 
        
        
        return len(nums) - res if res != -1 else -1