class Solution:
    def closestFair(self, n: int) -> int:
        cur = n
        ln = len(str(n))
        
        def returnOdd(ln):
            #all odd numbers handled
            if ln % 2:
                cur = '1'
                cur += ('0' * (math.ceil(ln / 2))) 
                cur += ('1' * (ln // 2))
                return int(cur)
        
        #print(cur)
        def check(num):
            odd = 0
            even = 0
            while num:
                if num % 10 % 2:
                    odd += 1
                else:
                    even += 1
                
                num //= 10
            
            return [odd == even, odd + even]
        
        
        while True:
            val = check(n)
            if val[0]:
                break
            elif val[1] % 2:
                return returnOdd(val[1])
            n += 1
        
        return n
        
        
            