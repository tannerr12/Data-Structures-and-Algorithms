class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        
        def isGood(val):
            if val == 0:
                return False
            h = 0
            for i in range(len(dist)):
                
                if i != len(dist) -1:
                    #print(val)
                    h += math.ceil(dist[i] / val)
                else:
                    h += dist[i] / val
            
            
            return h <= hour
        
        l,r = 0, 10**9
        res = -1
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid) and mid !=0:
                res = mid
                r = mid -1
            else:
                l = mid +1
        
        return int(res)