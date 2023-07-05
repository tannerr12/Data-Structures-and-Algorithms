class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        consec = 0
        last = 'a'
        res = ''
        while a or b:
            if a and not b:
                res += 'a' * a
                a = 0
            elif b and not a:
                res += 'b' * b
                b = 0
            elif a > b:
                res += 'aab'
                a -=2
                b -=1
            elif b > a:
                res += 'bba'
                b-=2
                a-=1
            else:
                res += 'ab' * a
                a = 0
                b = 0
                
            
        return res
            
            
            