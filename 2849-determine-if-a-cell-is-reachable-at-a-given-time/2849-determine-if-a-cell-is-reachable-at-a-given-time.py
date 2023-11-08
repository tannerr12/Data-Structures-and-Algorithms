class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

         
        return False if ([sx,sy] == [fx,fy] and t == 1) else max(abs(sx-fx), abs(sy-fy)) <= t