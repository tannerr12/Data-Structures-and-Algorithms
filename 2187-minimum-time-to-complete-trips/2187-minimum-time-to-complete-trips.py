class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def isGood(val):
            
            trips = 0 
            for i in range(len(time)):
                trips += val // time[i]
                if trips >= totalTrips:
                    return True
            return False
                
        
        
        l,r = 0, 10**14
        res= 0
        while l <= r:
            
            mid = (l+r)//2
            
            if mid != 0 and isGood(mid):
                res = mid
                r = mid -1
            else:
                l = mid +1
        return res