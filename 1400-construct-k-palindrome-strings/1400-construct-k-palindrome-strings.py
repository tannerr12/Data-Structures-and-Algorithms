class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        count = Counter(s)
        
        #print(count)
        ones = 0 
        twos = 0
        
        for key,val in count.items():
            if val % 2:
                ones +=1
            
            twos += val // 2
        
        #print(ones)
        #print(twos)
        
        while k > 1:
            
            if ones:
                ones -=1
            
            elif twos:
                if k > twos:
                    ones = 1
                    twos -=1
                else:
                    twos -=1
            else:
                return False
            
            k -=1
        
        
        return ones <= 1 and twos or ones == 1