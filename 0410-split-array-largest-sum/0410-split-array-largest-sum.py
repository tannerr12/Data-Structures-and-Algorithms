class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        
        def isGood(val):
            
            split = k-1
            local = 0
            for i in range(len(nums)):
                
                if local + nums[i] > val:
                    split -=1
                    local = nums[i]
                else:
                    local += nums[i]
                
                if split < 0:
                    return False
            return split >= 0
        
        l, r = max(nums), sum(nums)
        res = 0
        while l <= r:
            
            mid = (l+r) //2
            
            if isGood(mid):
                res = mid
                r = mid - 1
                
            else:
                l = mid +1
                
        
        return res
                