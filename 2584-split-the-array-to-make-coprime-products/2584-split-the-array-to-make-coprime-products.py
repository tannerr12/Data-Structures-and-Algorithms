
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        #mx = max(nums)
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
        
        
        #there are two ways that we can solve prime factorization the first is to use sleve method and gather all primes up to a certain point 
        #than go through each number and // by primes until the value is 1 but in this case that would be too slow
        
        #the second way to solve this problem is to do the prime factorization on the spot to do this we start at 2 and iterate all odds there after by saying if j is odd than j += 2 else j +=1
        #we can go up to 1000 than stop since we can assume everything past 1000 is concidered a "large prime" these can just be added as a prime on their own
        #once we have all the factors and indexes mapped out we can just loop through with 2 indexs one is to keep track of our current position and the other is to keep track of the furthest location where we have seen a common prime 
        #if the current index ever passes the max index than we can break and return our running index -1 since we can say there are no common primes past this point
 
        lastPrime = defaultdict(int)
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
 
            
                
                