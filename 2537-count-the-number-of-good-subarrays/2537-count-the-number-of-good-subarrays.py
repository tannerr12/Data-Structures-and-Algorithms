class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        #if greater than k add everything in between
        
        h = defaultdict(int)
        
        l = 0
        pairs = 0
        res = 0
        
        for i in range(len(nums)):
            
            h[nums[i]] +=1            
            if h[nums[i]] >= 2:
                pairs += h[nums[i]] - 1

            
            while pairs >= k: 
                h[nums[l]] -=1
                pairs -= h[nums[l]]
                l+=1    
                res += 1 + len(nums) - (i + 1) 
                
           
        return res