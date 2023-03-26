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
        
        while k:
            
            if ones:
                val = min(k,ones)
                k -= val
                ones -= val
            
            elif twos:
                if k > twos:
                    ones = 1
                    twos -=1
                    k-=1
                else:
                    return True
            else:
                return False
            
        
        
        
        return ones == 0