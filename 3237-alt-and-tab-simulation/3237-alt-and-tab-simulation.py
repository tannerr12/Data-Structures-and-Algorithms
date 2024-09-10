
class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        
        seen = set()
        arr = []
        
        for i in range(len(queries)-1,-1,-1):
            
            val = queries[i]
            if val not in seen:
                arr.append(val)
                seen.add(val)
                
            
            
        
        for i in range(len(windows)):
            val = windows[i]
            if val not in seen:
                arr.append(val)
        
        return arr