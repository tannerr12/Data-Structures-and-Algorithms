class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        
        def isGood(val):
   
            h = 0
            for i in range(len(dist)):
                
                if i != len(dist) -1:
                    #print(val)
                    h += math.ceil(dist[i] / val)
                else:
                    h += dist[i] / val
            
            
            return h <= hour
        
        l,r = 0, max(dist) * 100
        res = -1
        while l <= r:
            
            mid = (l+r)//2
            
            if mid != 0 and isGood(mid):
                res = mid
                r = mid -1
            else:
                l = mid +1
        
        return int(res)