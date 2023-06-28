from typing import List
from functools import lru_cache

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()
        n = len(cuboids)

        @lru_cache(None)
        def dp(i: int) -> int:
            if i == -1:
                return 0

            res = cuboids[i][2]
            for j in range(i):
                if all(cuboids[i][k] >= cuboids[j][k] for k in range(3)):
                    res = max(res, dp(j) + cuboids[i][2])

            return res

        return max(dp(i) for i in range(n))
