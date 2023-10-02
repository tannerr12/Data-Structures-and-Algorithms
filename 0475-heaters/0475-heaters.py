class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def isGood(mid):
            
            rmax = 0
            hidx = 0
            rmax = heaters[0] + mid
            for i in range(len(houses)):
                
                while hidx < len(heaters) and (heaters[hidx] + mid < houses[i]):
                    hidx += 1
                
                if hidx >= len(heaters) or heaters[hidx] - mid > houses[i]:
                    return False
            
            return True
        
        
        
        l,r = 0, 10**9
        res = 0
        while l <= r:
            
            mid = (l + r) // 2
            
            if isGood(mid):
                r = mid - 1
                res = mid
                
            else:
                l = mid + 1
                
        
        return res