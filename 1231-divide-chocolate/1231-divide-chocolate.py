class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        def isGood(val):
            groups = k+1
            total = 0
            for i in range(len(sweetness)):
                total += sweetness[i]
                if total >= val:
                    total = 0
                    groups -=1
                    if groups == 0:
                        return True
                
            if groups <= 0:
                return True
            return False
        
        
        l,r = 1, 10**15
        res = 0
        while l <= r:
            
            mid = (l+r) //2
            
            if isGood(mid):
                res = mid
                l = mid + 1
                
            else:
                r = mid -1
        
        
        return res
                
            
        
        