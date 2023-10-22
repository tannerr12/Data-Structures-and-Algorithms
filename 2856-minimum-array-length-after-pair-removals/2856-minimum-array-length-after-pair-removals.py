
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
    
    
        l, r = 0, len(nums) // 2
        
        
        def isGood(mid):
            end = 1
            for i in range(mid,-1,-1):
                if nums[-end] == nums[i]:
                    return False
                
                end +=1
        
            return True
        
        while l < r:
            
            mid = (l+r)// 2
            
            if isGood(mid):
                l = mid + 1
            
            else:
                r = mid
                
    
        return len(nums) - (l * 2)
                
    
        