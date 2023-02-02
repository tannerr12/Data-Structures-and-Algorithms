class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        
        
        dist = {}
        
        l = 0
        res = [0] * (len(nums) -k +1)
        for i in range(len(nums)):
            
            
            if nums[i] in dist:
                dist[nums[i]] +=1
            else:
                dist[nums[i]] = 1
                    
            
            while i - l + 1 > k:
                
                dist[nums[l]] -=1
                
                if dist[nums[l]] == 0:
                    del dist[nums[l]]
                    
                
                l += 1
            
            if i - l + 1 == k:
                res[i - k+1] = len(dist)
        
        return res
                
            
            