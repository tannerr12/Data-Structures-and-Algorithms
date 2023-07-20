class Solution:
    # We can first address the case it which it is impossible to merge to 1 element as in Example 2:
    # In each merge, length of stones reduces by k-1
    # If n - m*(k-1) cannot reach 1, we must return -1 (or infinity when we calculate cost)
    # Then we go into the test cases which are ok
    # This problem involves minimizing cost, let's think backward from the final state
    # As an example, stones = [3,5,1,2,6], k = 3
    # At final state we know it must be stones = [17], cost = 17, which is the sum of all stones
    # The minimum cost might come from merging [9,2,6], [3,8,6] or [3,5,9]
    # Translating the logic, we are trying to get what is the minimum cost to get stones into k (= 3 in this case) piles
    # Then each element might come from a merge
    # i.e. 9 comes from [3,5,1] (stones[0:3]), 8 comes from [5,1,2] (stones[1:4]) and 9 comes from [1,2,6] (stones[2:5])
    # We are seeing a recursive relation and a minimization among different options.
    # Therefore the top-down DP approach is first thing to try.
    # Here we define dp[i][j][m] = minimum cost to split nums[i:j+1] into m piles
    # Base cases: dp[i][i][m] = 0 for m = 1, otherwise inf (one element, can only break into 1 pile)
    # dp[i][j][m] = inf if (j+1-i-m) % (k-1) != 0 
    # (Try for example: stones = [3,5,1,2,6], k = 3, m = 2, i=0, j=4)
    # Recurrence relation:
    # dp[i][j][1] = dp[i][j][k] + sum(nums[i:j+1])
    # dp[i][j][m] = min(dp[i][K][1] + dp[K+1][j][m-1]), loop K from i to j-1, progress by k-1 to avoid getting infinities
    # We want to know what is dp[0][n-1][1]
    

        
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        
        #calculate if its even possible to merge this array size into 1 pile each merge removes k - 1 stones
        if (n-1) % (k-1) != 0:
            return -1
        
        memo = {}
        prefix = [0]
        
        for stone in stones:
            prefix.append(prefix[-1] + stone)
        
        @cache
        def dp(i,j,m):
            
            if i == j:
                if m == 1:
                    return 0
                else:
                    return float('inf')
                
            res = float('inf')
            if m == 1:
                res = dp(i,j,k) + prefix[j+1] - prefix[i]
            else:
                
                for K in range(i, j, k-1):
                    res = min(res, dp(i, K, 1) + dp(K+1, j, m-1))
                
            
            
            return res
            
            
                
            
        return dp(0,len(stones)-1,1)