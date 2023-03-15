class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        res = set()
        i = 0
        while x ** i <= bound:
            v1 = x ** i
            j = 0
            while (y ** j) + v1 <= bound:
                v2 = y ** j
                res.add(v1 + v2)
                if y == 1:
                    break
                j+=1
                
            if x == 1:
                break
            i+=1
        
        
        return list(res)