class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        
        words = s.split(' ')
        mx = 0
        for i in range(len(words)):
            mx = max(mx,len(words[i]))
        res = []
        
        for i in range(mx):
            w = ''
            wseen = False
            for j in range(len(words)-1,-1,-1):
                if i < len(words[j]):
                    wseen = True
                    
                if wseen and i < len(words[j]):
                    w = words[j][i] + w
                elif wseen:
                    w = ' ' + w
            
            res.append(w)
            
        
        return res
            
            
            
        
        