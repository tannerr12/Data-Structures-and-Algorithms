class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        
        
        h = set()
        
        
        for val in arr:

            if val * 2 in h or val / 2 in h:
                return True
            
            h.add(val)
        return False
            
        
     