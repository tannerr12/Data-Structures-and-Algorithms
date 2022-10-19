class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        res = left
        if left > 10000 and right - left > 10:
            left = left // (10 * len(str(left)) - 1)
        if right > 10000 and right - left > 10:
            right = right //(10 * len(str(right)) - 1)
        
        for i in range(left,right +1):
            
            
            res &= i
            if res == 0:
                break
            
        return res
            