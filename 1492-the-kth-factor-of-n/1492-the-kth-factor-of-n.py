class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        
        factors = []
        factorsback = []
        i = 1
        backcount = -1
        while i <= sqrt(n):
            
            if n % i == 0:
                
                factors.append(i)
                if i != sqrt(n):
                    factorsback.append(n // i)
                
            
            i +=1
        

        factorsback.reverse()
        newFact = factors + factorsback
        
        #print(newFact)
        if len(newFact) < k:
            return -1
        else:
            return newFact[k-1]
    