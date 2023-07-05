class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        res = ''
        
        if a > b:
            dist = min(b, (a-b))
            res += 'aab' * dist
            a -= 2 * dist
            b -= dist
        elif b > a:
            dist = min(a, (b-a))
            res += 'bba' * dist
            b -= 2 * dist
            a -= dist
        
        
        if a == b:
            
            res += 'ab' * a
            a=0
            b=0
        
        res += 'a' * a
        res += 'b' * b
        

        return res
            
            
            