class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        d = a | b
        
        res = 0
        for i in range(32):
            
            if c & (1 << i) > 0 and d & (1 << i) == 0:
                res += 1
            
            elif d & (1 << i) > 0 and c & (1 << i) == 0:
                if a & (1 << i) > 0 and b & (1 << i) > 0:
                    res += 2
                else:
                    res +=1
        
        return res