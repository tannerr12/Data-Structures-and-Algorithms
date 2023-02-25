class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        h = {}
        
 
            
        
        for i in range(len(nums)):
            
            a = nums[i]
            if a in h:
                if abs(h[a] - i) <=k:
                    return True
            h[a] = i  
            
            
        
        
        return False
            
            
            