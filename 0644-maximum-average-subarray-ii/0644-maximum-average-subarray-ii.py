class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        res = float('-inf')
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        for i in range(k, len(nums)+1):
            l = 0
            r = i
            while r < len(prefix):
                res = max(res, (prefix[r] - prefix[l]) / i)
                l+=1
                r+=1
        return res
        ''' 
            
            
        
        
        def isGood(val):
            currSum = 0
            prevSum = 0
            minSum = 0
            
            for i in range(len(nums)):
                currSum += nums[i] - val
                
                if i >= k-1 and currSum - minSum >= 0:
                    return True
                elif i >= k-1:
                    prevSum += nums[i-k+1] - val
                    minSum = min(minSum,prevSum)
                    
            
            return False
                    
        
        l,r = min(nums), max(nums)
        while r - l > 1e-5:
            
            mid = (l+r) / 2
            
            if isGood(mid):
                l = mid
            
            else:
                r = mid
        
        
        return l
        