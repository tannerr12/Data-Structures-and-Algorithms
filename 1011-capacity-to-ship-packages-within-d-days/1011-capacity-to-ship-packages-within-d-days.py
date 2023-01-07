class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l,r = max(weights), sum(weights)
        
        def isGood(val):
            
            res = 1
            localw = 0
            for i in range(len(weights)):
                if localw + weights[i] <= val:
                    localw += weights[i]
                else:
                    res +=1
                    localw = weights[i]
                
                if res > days:
                    return False
            
            return res <= days
                
        
        res = float('inf')
        while l <= r:
            
            mid = (l+r) //2
            
            if isGood(mid):
                res = mid
                r = mid -1
            
            else:
                l = mid +1
                
        
        return res
                