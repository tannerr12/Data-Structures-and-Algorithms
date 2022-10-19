class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        res = left
        if left > 10000 and right - left > 1000:
            left = left //10
        if right > 10000 and right - left > 1000:
            right = right //10
        
        for i in range(left,right +1):
            
            
            res &= i
            if res == 0:
                break
            
        return res
            