class Solution:
    def clearStars(self, s: str) -> str:
        
        
        res = []
        
        
        identify = set()
        heap = []
        for i in range(len(s)):
            
            if s[i] == '*':
                if heap:
                    char,val = heappop(heap)
                    identify.add(-val)
                
            else:
                heappush(heap, (s[i], -i))
        
        #print(identify)
        
        for i in range(len(s)):
            if i not in identify and s[i] != '*':
                res.append(s[i])
                
        
        
        return ''.join(res)
                    
                
            