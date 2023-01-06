class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        dp = [0] * 26
        
        for c in s:
            
            v = ord(c) - ord('a')
            
            for i in range(max(0,v - k), min(26, v + k +1)):
                dp[v] = max(dp[i], dp[v])
            
            dp[v] +=1
        
        return max(dp)