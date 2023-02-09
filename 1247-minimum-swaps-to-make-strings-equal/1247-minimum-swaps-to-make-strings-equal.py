class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        
        c = Counter(s1 + s2)

        for key,val in c.items():
            if val % 2:
                return -1
         
        
        res = 0
        diffx = 0
        diffy = 0
        for x,y in zip(s1,s2):
            
            if x != y:
                if x == 'x':
                    diffx +=1
                else:
                    diffy +=1
                
                
        
        if diffx ==0 and diffy == 0:
            return 0
        
        
        res += diffx // 2
        if diffx % 2:
            res+=1
        res += diffy // 2
        if diffy % 2:
            res +=1

        return res
            
            
                