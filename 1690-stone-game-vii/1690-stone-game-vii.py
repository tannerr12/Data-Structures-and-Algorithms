class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = [0]
        for i in range(len(stones)):
            prefix.append(prefix[-1] + stones[i])
        
     
        @lru_cache(maxsize = 100000)
        def dfs(i, j):
            
            if i > j:
                return 0
            turn = 1
            if (i + (len(stones) - 1 - j))  % 2:
                turn = -1
            res = 0
            if turn == 1:
                
                #take far right
                res = max(res, dfs(i+1,j) + ((prefix[j+1] - prefix[i+1]) * turn))
                #take far left
                res = max(res, dfs(i,j-1) + ((prefix[j] - prefix[i]) * turn))
            else:
                res = float('inf')
                #take far right
                res = min(res, dfs(i+1,j) + ((prefix[j+1] - prefix[i+1]) * turn))
                #take far left
                res = min(res, dfs(i,j-1) + ((prefix[j] - prefix[i]) * turn))
            
            return res
        
        
        return dfs(0, len(stones)-1)
            