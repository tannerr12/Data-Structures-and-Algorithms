class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        """
        primes = [2]
        
        def checkPrime(i):
            
            for j in range(2,i):
                if i % j ==0:
                    return False
            
            return True
        
        for x in range(3,1001,2):
            if checkPrime(x):
                primes.append(x)
            
        """
        #print(primes)
        res = set()
        
        for x in nums:
            n = x
            i = 2
            while i < 1000 and n != 1:
    
                if n % i == 0:
                    res.add(i)
                while n % i == 0:
                    n//=i
                
                i += 1 + i % 2
        
        
        return len(res)
                
                