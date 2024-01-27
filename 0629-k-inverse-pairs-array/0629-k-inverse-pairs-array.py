class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def fn(n, k):
            """Return number of ways for n numbers with k inverse pairs."""
            if k == 0: return 1 
            if n <= 0 or k < 0: return 0 
            return fn(n-1, k) + fn(n, k-1) - fn(n-1, k-n)
        
        return fn(n, k) % 1_000_000_007