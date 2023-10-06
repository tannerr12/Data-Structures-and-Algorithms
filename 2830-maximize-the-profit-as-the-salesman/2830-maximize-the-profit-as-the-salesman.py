class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        
        offers.sort(key=lambda x: (x[1]))
        '''
        0 -> 0 + val = 1
        
        1 
        
        2 - > mx current, -1 + val 
        
        3 -> current, 0 + val 
        
        
        0 = 1
        
        1 = 1
        
        2 = 2
        
        3 = 1 + 2
        
        
        ans = 3
        

        '''
        
        
        dp = [0] * (n+1)
        idx = 0
        for i in range(n):
            best = dp[i]
            while idx < len(offers) and offers[idx][1] == i:
                #find max
                start = offers[idx][0] 
                val = offers[idx][2]
                best = max(best,dp[start] + val)
                
                idx += 1
                
            dp[i+1] = best
        
        
        return dp[-1]