from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return factorial(m + n - 2) // (factorial(n - 1) * factorial(m - 1))
