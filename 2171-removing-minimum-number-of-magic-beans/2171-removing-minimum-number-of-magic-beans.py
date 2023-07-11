class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        
        left = sum(beans)
        right = 0
        
        res = float('inf')
        for i in range(len(beans)-1,-1,-1):
            left -= beans[i]
            r = right - (beans[i] * (len(beans) -1 - i))
            total = left + r
            res = min(res, total)
            
            right += beans[i]
        
        return res