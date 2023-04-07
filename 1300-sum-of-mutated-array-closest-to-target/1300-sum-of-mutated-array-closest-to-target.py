class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        #2,3,5
        #2,3,5 = 10
        
        #1,2,3,4,5
        #3  6  8  9  10
        
        #in the case of a tie or greater we check lower
        #in the case of lower we check greater
        
        def isGood(val):
            
            tot = 0
            
            for v in arr:
                
                if v > val:
                    tot += val
                else:
                    tot += v
            
            return tot
        
        
        
        l, r = 0, max(arr)
        
        
        res = [float('inf'), 0]
        
        while l <= r:
            
            mid = (l+r) // 2
            
            val = isGood(mid)
            
        
            if abs(target - val) == res[0] and mid < res[1]:
                res = [abs(target - val), mid]
            elif abs(target - val) < res[0]:
                res = [abs(target - val), mid]
            
            if val >= target:
                r = mid -1
            else:
                l = mid + 1
        
        
        
        return res[1]