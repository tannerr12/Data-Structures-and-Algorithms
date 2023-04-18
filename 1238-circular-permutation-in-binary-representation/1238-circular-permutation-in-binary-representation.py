class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        
        res = []
        pos = 0
        for i in range(2**n):
            res.append(i ^ (i >> 1))
            if res[-1] == start:
                pos = i
        
        
        
        return res[pos:] + res[:pos]