class Solution:
    def stoneGameVI(self, av: List[int], bv: List[int]) -> int:
        

        diff = []
        
        for i in range(len(av)):
            diff.append((av[i] + bv[i],i))
            
        
        diff.sort(reverse=True)
        
        
        alice = 0
        bob = 0
        
        for i in range(len(diff)):
            val,pos = diff[i]
            
            if i % 2 == 0:
                alice += av[pos]
            else:
                bob += bv[pos]
                
        
        
        if alice > bob:
            return 1
        elif bob > alice:
            return -1
        else:
            return 0
            
            
        
        
        
            
        
        
        