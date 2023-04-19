class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
   
        v1,v2 = str(digit1),str(digit2)
        
        x =[v1,v2]
        
        arr = itertools.product(x, repeat=10)
        mx = 2 ** 31 -1
        res = float('inf')
        for p in list(arr):
            p = list(p)
            while p:
                num = int(''.join(p))

                if num > k and num % k == 0 and num <= mx:
                    res = min(res,num)

                p.pop()
            
      
        return res if res != float('inf') else -1 
            
            