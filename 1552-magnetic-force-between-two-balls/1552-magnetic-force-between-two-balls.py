class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def isGood(mid):
            balls = m
            last = -1
            for i in range(len(position)):
                if last == -1 or (position[i] - last) >= mid:
                    balls -= 1
                    last = position[i]
                
                if balls == 0:
                    break
            
            return balls == 0
                
        
        
        l,r = 1, max(position) - m + 1
        res = 1
        while l <= r:
            
            mid = (l+r)// 2
            
            if isGood(mid):
                res = mid
                l = mid + 1
            
            else:
                
                r = mid - 1
        
        
        return res