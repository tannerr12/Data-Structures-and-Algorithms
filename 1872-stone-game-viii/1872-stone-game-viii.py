class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        @cache
        def dfs(i):
            if i == len(stones)-2:
                return preSum[-1]
            
            kt = dfs(i+1)
            st = preSum[i+1] - dfs(i+1)
            
            return max(kt,st)
        
        preSum = list(accumulate(stones))
        return dfs(0)
                