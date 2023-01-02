class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        
  
        helper(start, m) := the max stones that the first player will get with given piles[start:] and M.
        max_stones = MAX{ (sum of all the stones) - (max_stones the other player will get) } = MAX{ sum(piles[start:]) - helper(start+x, max(m, x)) }

        class Solution(object):
            def stoneGameII(self, piles):
                def helper(start, m):
                    if (start, m) in history: return history[(start, m)]

                    if start>=len(piles): return 0
                    if start+m*2>=len(piles): return sum(piles[start:])

                    max_stones = float('-inf')
                    for x in xrange(1, m*2+1):
                        max_stones = max(max_stones, sum(piles[start:])-helper(start+x, max(m, x)))

                    history[(start, m)] = max_stones
                    return history[(start, m)]

                history = {}
                return helper(0, 1)


        Similar Problems: 312, 664, 1024, 1039, 1140, 1130
        For more other topics similar problems, check out my GitHub.
        It took me a lots of time to make the solution. Becuase I want to help others like me.
        Please give me a star if you like it. Means a lot to me.
        https://github.com/wuduhren/leetcode-python

        """
        #get the max score from the opposing player and subtract it from the max total to get
        #Alice total
        @cache
        def dfs(i,m):
            if i >= len(piles):
                return 0
            if i + m*2 >= len(piles):
                return sum(piles[i:])

            maxStones = float('-inf')
            for j in range(1,(m *2)+1):
                maxStones = max(maxStones, sum(piles[i:]) - dfs(i+j, max(m,j)))
            
            
        
            return maxStones
                
                
            
        return dfs(0,1)
        
            