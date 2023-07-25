class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        c = Counter(num)
        ans = ''
        for i in range(9,-1,-1):
            n = str(i)
            if c[n] > 1:
                if n == '0' and len(ans) == 0:
                    continue
                count = c[n] // 2
                ans += n * count
                c[n] = c[n] % 2
        
        right = ans[::-1]
    
        
        for i in range(9,-1,-1):
            n = str(i)
            if c[n] == 1 or (c[n] > 0 and n == '0' and len(ans) == 0): 
                ans += n
                c[n] = 0
                break
        
        ans += right
        return ans