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
        while r - l > 1e-6:
            mid = (l+r)/2
            
            if isGood(mid):
                res = mid
                r = mid 
            else:
                l = mid 
                
        return res
        