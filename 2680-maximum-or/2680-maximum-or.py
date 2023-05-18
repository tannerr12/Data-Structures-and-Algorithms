class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
 
        prefix = [0] 
        suffix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] | prefix[-1])
        
        for i in range(len(nums)-1,-1,-1):
            suffix.append(nums[i] | suffix[-1])
        suffix.reverse()
        res = 0
        
        for i in range(len(nums)):    
            res = max(res, (nums[i] << k) | prefix[i] | suffix[i+1])
        
        
        return res
            
            
        
        
        