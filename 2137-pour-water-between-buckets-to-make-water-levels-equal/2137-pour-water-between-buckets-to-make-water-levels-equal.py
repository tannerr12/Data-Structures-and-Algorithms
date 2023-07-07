class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        total = sum(buckets)
        
        def isGood(mid):
            count = 0
            dist = (100 - loss) / 100
            for i in range(len(buckets)):
                if buckets[i] <= mid:
                    count -= mid - buckets[i]
                else:
                    count += (buckets[i] - mid) * dist
            
            return count >= 0
        
        
        
        l,r = 0, total
        res = 0
        
        d = 1e-6
        #print(d)
        while abs(l - r) >= d:
            
            mid = (l+r)/2
            
            if isGood(mid):
                res = mid
                l = mid + d
            else:
                r = mid - d
        
        return res
                