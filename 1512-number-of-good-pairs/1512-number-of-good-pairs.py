class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        res = 0 
        
        for key in c:
            
            res += (c[key] * (c[key] -1)) // 2
            
        
        return res

    
       
        
        
        