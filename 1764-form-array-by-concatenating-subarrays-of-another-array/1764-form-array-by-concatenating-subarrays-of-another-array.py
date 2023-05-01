class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        
        
        i = 0
        j = 0
        while j < len(groups) and i < len(nums):
            
            if nums[i] == groups[j][0]:
                
                l = len(groups[j])
                if nums[i:i+l] == groups[j]:
                    i += l 
                    j+=1
                else:
                    i+=1
            else:
                i+=1
        
        
        
        return j >= len(groups)
        
        
                
            