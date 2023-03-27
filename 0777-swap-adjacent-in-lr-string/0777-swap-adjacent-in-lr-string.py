class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        countS = Counter(start)
        countE = Counter(end)
        
        if countS != countE:
            return False
        #cant get R past L
        
        #try one pass each way
        
        need = 0
        for i in range(len(start)):
            if start[i]== 'L' and end[i] != 'L' and need == 0:
                return False
            elif end[i] == 'L' and start[i] != 'L':
                if start[i] == 'R':
                    return False
                
                need +=1
            
            elif need and start[i] == 'R':
                return False
            
            elif need and start[i] == 'L' and end[i] != 'L':
                need -=1
        
        
        if need:
            return False
        
        
        need = 0
        for i in range(len(start)-1,-1,-1):
            if start[i]== 'R' and end[i] != 'R' and need == 0:
                return False
            if end[i] == 'R' and start[i] != 'R':
                if start[i] == 'L':
                    return False
                
                need +=1
            
            elif need and start[i] == 'L':
                return False
            
            elif need and start[i] == 'R' and end[i] != 'R':
                need -=1
                
        
        if need:
            return False
        
        return True
        