class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n ==1:
            return 1
        heap = primes.copy()
        n-=1
        
        while n:
            val = heappop(heap)
            n-=1
            if n ==0:
                return val
            
            for v in primes:

                heappush(heap, val * v) 
                if val % v == 0:
                    break
              
                
            
            
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
                