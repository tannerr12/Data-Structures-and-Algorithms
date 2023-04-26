class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        for i in range(n+1, 10**7):
            
            count = Counter(str(i))
            found = True
            for key,val in count.items():
                
                if int(key) != val:
                    found = False
                    break
                    
            
            if found:
                return i
            
        
        
    
            
            
            