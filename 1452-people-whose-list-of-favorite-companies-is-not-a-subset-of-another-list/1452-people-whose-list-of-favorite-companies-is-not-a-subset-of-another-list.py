class Solution:
    def peopleIndexes(self, fc: List[List[str]]) -> List[int]:
        
        res = []
        for i in range(len(fc)):
            fc[i] = set(fc[i])

        for i in range(len(fc)):
            found = False
            for j in range(len(fc)):
                
                if i == j:
                    continue
                    
                if fc[i] <= fc[j]:
                    found = True
                    break
                    
            
            if not found:
                res.append(i)
                
        
        
        return res