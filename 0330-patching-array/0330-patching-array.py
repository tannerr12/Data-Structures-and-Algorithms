class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        
        i,res,upto = 0,0,0
        
        while upto < n:
            
            if i < len(nums) and upto + 1 >= nums[i]:
                upto += nums[i]
                i+=1
            else:
                upto += (upto + 1)
                res += 1
        
        
        return res