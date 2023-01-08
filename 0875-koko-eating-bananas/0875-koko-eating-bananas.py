class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        
        def isGood(val):
            
            hour = 0
            for i in range(len(piles)):
                
                hour += math.ceil(piles[i] / val)
                
                if hour > h:
                    return False
                
            return hour <= h
                
        
        l,r = 1, max(piles)
        res = 0
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                res = mid
                r = mid -1
            else:
                l = mid +1
            
        return res
                
                
                