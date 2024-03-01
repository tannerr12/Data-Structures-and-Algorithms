class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        
        directions = [[1,0], [1,1], [0,1],[1,-1],[-1,1], [-1,0], [0,-1], [-1,-1]]
        
        #primes = [True] * (10**(max(len(mat), len(mat[0]))))
        '''
        def gatherPrimes():
            cur = 2
            mx = isqrt(10**(max(len(mat), len(mat[0]))))
            
            while cur < mx:
                if primes[cur] == True:
                    tcur = cur * cur
                    while tcur < (10**(max(len(mat), len(mat[0])))):
                        primes[tcur] = False
                        tcur += cur

                
                cur += 1
        '''
        #gatherPrimes()
        
        @cache
        def isPrime(x):
            for i in range(2, isqrt(x)+1):
                if x % i == 0:
                    return False
            
            return True
                
            
        
        mp = defaultdict(int)
        def isGood(x,y):
            
            return x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0])
        #6 * 6 * 8 * 6
        for i in range(len(mat)):
            for j in range(len(mat[0])):
   
                #try all 8 directions
                for x,y in directions:
                    curx,cury = i,j
                    num = 0
                    while isGood(curx,cury):
                        num *= 10
                        num += mat[curx][cury]
                        if mat[curx][cury] % 2 and num > 10 and isPrime(num):
                            mp[num] += 1
                            
                        curx += x
                        cury += y
        
        if len(mp) == 0:
            return -1
        mx = max(mp.values())
        res = -1
        for key,val in sorted(mp.items()):
            if val == mx:
                res = key
        
        return res
        