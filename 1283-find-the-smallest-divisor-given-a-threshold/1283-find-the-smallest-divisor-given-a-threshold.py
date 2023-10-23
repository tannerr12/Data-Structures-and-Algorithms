class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def isGood(mid):
            
            val = 0
            for i in range(len(nums)):
                val += math.ceil(nums[i] / mid)
                
            
            return val <= threshold
        
        
        l,r = 1, 10 ** 6
        res = 0
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1
                
                
        
        return res
            