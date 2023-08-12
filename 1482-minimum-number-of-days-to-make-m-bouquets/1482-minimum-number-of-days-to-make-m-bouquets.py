class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def isGood(mid):
            streak = 0
            count = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    streak += 1
                    if streak == k:
                        count += 1
                        streak = 0
                else:
                    streak = 0
            
            return count >= m
                    
        
        
        res = -1
        
        l, r = 0, 10 ** 9
        
        while l <= r:
            
            mid = (l+r) // 2
            
            if isGood(mid):
                r = mid -1
                res = mid
                
            else:
                l = mid + 1
        
        
        return res
                
                