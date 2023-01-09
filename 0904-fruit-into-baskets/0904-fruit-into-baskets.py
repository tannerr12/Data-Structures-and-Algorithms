class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        localSum =1
        globalSum =1
        
        h = {}
        h[fruits[0]] =1
        l,r = 0,1
        
        while r < len(fruits):
            
            if len(h) < 2 or fruits[r] in h:
                if fruits[r] in h:
                    h[fruits[r]] +=1
                else:
                    h[fruits[r]] = 1
                    
            else:
                
                while len(h) == 2:
                    
                    fruit = fruits[l]
                    h[fruit] -= 1
                    if h[fruit] ==0:
                        del h[fruit]
                    l +=1
                h[fruits[r]] = 1
            
            localSum = max(localSum, sum(h.values()))
            r +=1
        
        return localSum
        
                
                
                
                