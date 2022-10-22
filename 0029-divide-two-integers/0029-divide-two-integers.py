class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        res = 0
        
        tdividend = dividend
        tdivisor = divisor
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        
        while dividend - divisor >= 0:
            
            x= 0
            
            while dividend >= (divisor << 1 << x):
                x+=1
            
            
            dividend -= divisor << x
            
            res += 1 << x
            
        
       
        return res if (tdivisor >= 0) == (tdividend >= 0) else -res