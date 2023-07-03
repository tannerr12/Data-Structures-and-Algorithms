class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        
        def isGood(mid):
            op = maxOperations
            for i in range(len(nums)):
                if nums[i] > mid:
                    opneeded = math.ceil(nums[i] / mid) - 1
                    op -= opneeded
                    if op < 0:
                        return False
            
            return True
            
        
        l,r = 1,10 ** 9
        res = float('inf')
        while l <= r:
            
            mid = (l+r) // 2
            
            if isGood(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
                
        
        return res
                
            