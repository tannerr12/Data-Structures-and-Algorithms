class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        """
        target 21
        
        
        7,8,9,10,11,12,13,14,15,16 - > 17,18,19,20,21,22,23,24,25,26
                                        10  9  8  7  6  5  4  3  2  1 
            
            55
            
            40
            21
            
            72.7 %
            
        0, -> 1,2,3,4,5,6,7,8,9,10
              1 1 1 1 1 1 1 1 1 1
            6/10 = 0.60
            
            
    0  1, 2, 3 -> 4, 5
    1  1  2  3    5  3
            
       0 -> 1 or 2
       
       1 
       1
        """
        
        n = min(n,k-1+ maxPts)
        dp = [0] * (n +1)
        
        dp[0] = 1.0
        running = 0
        
        
        for i in range(1,n+1):
            if i-1 < k:
                running += dp[i-1]
            if i - 1 - maxPts >= 0:
                running -= dp[i-1-maxPts]
                
            
            dp[i] = 1/maxPts * running
        
        
 
        return sum(dp[k:n+1])