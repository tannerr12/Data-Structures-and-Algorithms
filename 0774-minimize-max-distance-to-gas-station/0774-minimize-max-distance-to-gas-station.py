class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        
        arr = []
        
        for i in range(len(stations)-1):
            arr.append(stations[i +1] - stations[i])
        
        
        def isGood(val):
            sta = k
            for i in range(len(arr)):
               
                if arr[i] > val:
                    v = math.ceil(arr[i] / val)
                    v-=1
                    sta -= v
                if sta < 0:
                    return False
            
            return sta >= 0
                
        
        
        l,r = 0, max(arr)

        res = 0
        while l<=r:
            mid = (l+r)/2
            
            if isGood(mid):
                res = mid
                r = mid - 0.00000001
            else:
                l = mid + 0.00000001
                
        return res
        