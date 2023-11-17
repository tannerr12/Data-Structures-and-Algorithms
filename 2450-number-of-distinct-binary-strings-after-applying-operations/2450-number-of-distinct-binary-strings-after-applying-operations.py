class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        res = pow(2, len(s) - k +1, MOD)
       
        return res
            
            