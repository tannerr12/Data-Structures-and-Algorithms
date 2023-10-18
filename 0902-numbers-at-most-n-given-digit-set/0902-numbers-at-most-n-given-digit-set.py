class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        D = list(map(int, D))
        N = list(map(int, str(N)))

        @functools.lru_cache(None)
        def dp(i, isPrefix, isBigger):
            if i == len(N):
                return not isBigger
            if not isPrefix and not isBigger:
                return 1 + len(D) * dp(i + 1, False, False)
            return 1 + sum(dp(i + 1, isPrefix and d == N[i], isBigger or (isPrefix and d > N[i])) for d in D)

        return dp(0, True, False) - 1