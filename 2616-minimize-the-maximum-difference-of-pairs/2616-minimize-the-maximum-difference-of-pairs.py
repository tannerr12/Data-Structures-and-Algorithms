class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        
        def isGood(val):
            
            k = p
            i = 1
            while i < len(nums):
                if k <=0:
                    return True
                if nums[i] - nums[i-1] <= val:
                    k -=1
                    i +=1
                i +=1
            
            if k <= 0:
                return True
            else:
                return False
        
        l,r = 0,10**9
        res = float('inf')
        while l <= r:
            
            mid = (l+r)// 2
            
            if isGood(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        
        
        return res