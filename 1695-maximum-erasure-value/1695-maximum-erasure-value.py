class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        
        cur = 0
        l = 0
        res = 0
        count = defaultdict(int)
        for i, val in enumerate(nums):
            
            count[val] +=1
            cur +=val
            
            while count[val] > 1:
                
                count[nums[l]] -=1
                cur -= nums[l]
                l+=1
            
            
            
            res = max(res,cur)
            
        
        
        return res
            
            
                
            
            