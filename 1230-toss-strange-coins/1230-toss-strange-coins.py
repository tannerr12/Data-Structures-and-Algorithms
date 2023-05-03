class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
    
        n = len(prob)
        dp =[0] * (target + 1)
        
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(target, 0, -1):
                dp[j] =  dp[j-1] * prob[i-1] + dp[j] * (1-prob[i-1])
            
            dp[0] = dp[0] * (1- prob[i-1])
        
        
        return dp[target]
        '''
        @cache
        def dfs(i,head):

            if i >= len(prob):
                if head == target:
                    return 1
                else:
                    return 0
            
            res = 0
            #flip heads or tails
            res = (dfs(i+1, head + 1) * prob[i]) + (dfs(i+1, head) * (1 - prob[i]))

            return res
        
        
        return dfs(0, 0)
        '''