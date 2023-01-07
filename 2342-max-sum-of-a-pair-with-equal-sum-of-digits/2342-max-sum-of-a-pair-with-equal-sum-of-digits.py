class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        h = {}
        res = -1
        for i in range(len(nums)):
            lr = 0
            s = str(nums[i])
            
            for x in s:
                lr += int(x)
            
            if lr in h:
               
                res = max(res, nums[i] + h[lr])
                h[lr] = max(h[lr], nums[i])
            else:
                h[lr] = nums[i]
            
        
        return res
            