class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        # Python 3 program to check
        # Euclid Number
        MAX = 10000

        arr = []

        # Function to generate prime numbers
        def SieveOfEratosthenes(n):

            # Create a boolean array "prime[0..n]"
            # and initialize all entries it as
            # true. A value in prime[i] will
            # finally be false if i is Not a
            # prime, else true.
            prime = [True] * n

            p = 2
            while p * p < n:

                # If prime[p] is not changed,
                # then it is a prime
                if (prime[p] == True):

                    # Update all multiples of p
                    for i in range(p * 2, n, p):
                        prime[i] = False

                p += 1

            # store all prime numbers
            # to vector 'arr'
            for p in range(2, n):
                if (prime[p]):
                    arr.append(p)
                
            
            return arr
        

        arr = SieveOfEratosthenes(n)
        
        #print(arr)
        
        s = set(arr)
        #print(s)
        ans = []
        for val in sorted(s):
            if val > n // 2:
                break
            target = n - val
            if target in s:
                ans.append([val, target])
            
        
        return ans
        