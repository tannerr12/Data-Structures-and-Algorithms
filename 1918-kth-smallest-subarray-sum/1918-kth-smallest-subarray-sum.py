class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        def isGood(x):
            
            cur = 0
            cnt = 0
            l = 0
            for i in range(len(nums)):
                
                cur += nums[i]
                
                while cur > x:
                    cur -= nums[l]
                    l+=1
                
                cnt += i - l + 1
            
            return cnt >= k
        
        
        
        n = len(nums)
        
        l,r = 0, 10**9
        res = 0
        while l <= r:
            
            mid = (l+r) // 2
            
            if isGood(mid):
                res = mid
                r = mid -1
            
            else:
                
                l = mid + 1
                
        
        
        return res
                
                
            
        
        
        
        