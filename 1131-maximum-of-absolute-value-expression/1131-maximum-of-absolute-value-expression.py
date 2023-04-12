class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        
        mn = [float('inf')] * 4 
        mx = [float('-inf')] * 4
        
        res = 0
        #abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B).
        #4 possible combinations 
        #8 total to find min and max
        for i,(x,y) in enumerate(zip(arr1,arr2)):
            
            
            mx[0] = max(mx[0], x + y - i)
            mx[1] = max(mx[1], x - y - i)
            mx[2] = max(mx[2], -x + y - i)
            mx[3] = max(mx[3], -x - y - i)
            
            mn[0] = min(mn[0], x + y - i)
            mn[1] = min(mn[1], x - y - i)
            mn[2] = min(mn[2], -x + y - i)
            mn[3] = min(mn[3], -x - y - i)
            
            
            res = max(res, mx[0] - mn[0])
            res = max(res, mx[1] - mn[1])
            res = max(res, mx[2] - mn[2])
            res = max(res, mx[3] - mn[3])
            
        
        return res
            
            
            
            
            
            
            