class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n ==1:
            return 1
        vals = set()
        heap = primes.copy()
        
        n-=1
        
        while n:
            val = heappop(heap)
            vals.add(val)
            n-=1
            if n ==0:
                return val
            
            for v in primes:
                if v * val in vals:
                    continue
                heappush(heap, val * v)
                vals.add(val * v)
                
            
            
        '''
        for i in range(len(primes)):
            for j in range(i, len(primes)):
                vals.add(lcm(primes[i], primes[j]))
                
        print(vals)
        
        found = 0
        for i in range(1,(10**6) + 1):
            num = i
            for j in range(len(primes)):
                if num in p:
                    num = 1
                    break
                while num % primes[j] == 0:
                    num //= primes[j]
            
            
            if num == 1:
                found +=1
                if found == n:
                    return i
        
    
                
        '''     
        #print(found)
                