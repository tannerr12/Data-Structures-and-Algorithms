class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        mx = [float('-inf'),0]
        mn = [float('inf'),0]
        
        for i,val in enumerate(nums):
            
            if val > mx[0]:
                mx = [val, i]
            if val < mn[0]:
                mn = [val, i]
                
        
        #print(mx)
        #print(mn)
        
        l = len(nums)
        res = float('inf')
        #calculate all left
        res = min(res, max(mn[1], mx[1]) + 1)
        #calculate all right
        res = min(res, l - min(mn[1], mx[1]))
        #calculate mix
        res = min(res, l - max(mn[1], mx[1]) + min(mn[1], mx[1]) + 1)
        
        return res
            