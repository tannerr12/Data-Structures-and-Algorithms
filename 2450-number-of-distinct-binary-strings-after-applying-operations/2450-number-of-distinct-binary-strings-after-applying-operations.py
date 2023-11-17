class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        res = 1 
        
        for i in range(len(s) - k+1):
            res *= 2
            res %= MOD
        
        return res
            
            