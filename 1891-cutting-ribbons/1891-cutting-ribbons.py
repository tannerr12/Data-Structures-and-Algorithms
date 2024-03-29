class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        
        def isGood(mid):
            need = k
            for i in range(len(ribbons)):
                
                need -= ribbons[i] // mid
                if need <= 0:
                    return True
            
            return False
                
                
        
        l,r = 1, 10 ** 9
        res = 0
        
        while l <= r:
            
            mid = (l+r) //2 
            
            if isGood(mid):
                res = mid
                l = mid + 1
            else:
                r = mid -1
        
        return res