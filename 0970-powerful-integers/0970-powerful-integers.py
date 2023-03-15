class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        i =0
        ls1 = []
        ls2 = []
        
        if x == 1:
            ls1 = [1]
        else:
            while x ** i < bound:
                ls1.append(x ** i)
                i+=1
        
        i = 0
        
        if y == 1:
            ls2 = [1]
        else:
            while y ** i < bound:
                ls2.append(y**i)
                i+=1

                
        res = set()
        
        for i in range(len(ls1)):
            for j in range(len(ls2)):
                
                v1,v2 = ls1[i], ls2[j]
                if v1 + v2 > bound:
                    break
                res.add(v1 + v2)
        
        
        return list(res)