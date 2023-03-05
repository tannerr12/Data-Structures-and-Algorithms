
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        mx = max(nums)
        """
        primes = [True] * (mx)
        primes[0]=False
        primes[1]=False
        def findPrimes(n):
            
            
            for i in range(2,isqrt(n) +1):
                
                for j in range(i*i, n , i):
                    primes[j] = False
                    
            
            return primes
            
        
        findPrimes(mx//2)
    
        p = []
        
        for i,v in enumerate(primes):
            if v:
                p.append(i)
                
        """

 
        lastPrime = defaultdict(int)
        #print(p)
        factors = defaultdict(list)
        for i in range(len(nums)):
            
            #prime factorize
            val = nums[i]
            j = 2
            while j < 1000:
                if val % j == 0:
                    factors[i].append(j)
                    lastPrime[j] = i
                while val % j == 0:
                    val //= j
                
                    
                if val <= 1:
                    break
                j += 1 + j % 2
            if val > 1:
                factors[i].append(val)
                lastPrime[val] = i

        resultidx = 0
        it = 0
        
        while it <= resultidx:
            
            for fact in factors[it]:
                resultidx = max(resultidx, lastPrime[fact])
            it +=1
        
        if it == len(nums):
            return -1
        return it -1 
 
            
                
                