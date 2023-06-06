class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        
        s = sum(rods)
        
        
        dp = [-1] * (s + 1)
        
        dp[0] = 0
                 
        
        for rod in rods:
            current = dp.copy()
            
            for i in range(s - rod + 1):
                if current[i] < 0:
                    continue
            
                dp[i + rod] = max(dp[i+rod], current[i])
                dp[abs(i-rod)] = max(dp[abs(i-rod)], current[i] + min(i,rod))
                
        
        return dp[0]