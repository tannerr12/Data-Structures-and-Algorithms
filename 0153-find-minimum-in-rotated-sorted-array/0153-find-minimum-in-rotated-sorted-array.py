class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r = 0,len(nums) -1
        res = nums[0]
        while l <= r:
            if nums[r] > nums[l]:
                res = min(res,nums[l])
                break
            curr = (l+r)//2
            res = min(res,nums[curr])
            if nums[curr] >= nums[l]:
                l = curr +1
            else:
                r = curr -1
        
        
        return res