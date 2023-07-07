class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        total = sum(buckets)
        
        def isGood(mid):
            below = 0
            above = 0
            dist = (100 - loss) / 100
            for i in range(len(buckets)):
                if buckets[i] <= mid:
                    below += mid - buckets[i]
                else:
                    above += (buckets[i] - mid) * dist
            
            return below <= above
        
        
        
        l,r = 0, total
        res = 0
        
        d = 0.000001
        #print(d)
        while abs(l - r) >= d:
            
            mid = (l+r)/2
            
            if isGood(mid):
                res = mid
                l = mid + d
            else:
                r = mid - d
        
        return res
                