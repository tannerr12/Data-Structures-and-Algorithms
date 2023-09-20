class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        if n <= 0:
            return 0
        if n <= 9:
            return 1
        
        dp = defaultdict(int)
        dp[0] = 0
        dp[9] = 1
      
        
        #gather the result for all the 10s positions
        #10 + 10  
        #[0-9] + [10-19] + [20 - 99]
        i = 9
        while i <= 10 ** 9:
            dp[i * 10 + 9] = 10 * dp[i] + (i + 1) 
            i *= 10
            i += 9
        
        #ex 111
        
        #f(99) + f(11)
        
        temp = n
        div = 1
        
        while temp//10:
            
            temp //= 10
            div *= 10
        
        
        firstNum = n // div
        rem = n % div
        
        ans += firstNum * dp[div-1]
        ans += div if firstNum > 1 else 0
        ans += rem + 1 if firstNum == 1 else 0
        ans += self.countDigitOne(rem)
        return ans 
        
        
        
        
            