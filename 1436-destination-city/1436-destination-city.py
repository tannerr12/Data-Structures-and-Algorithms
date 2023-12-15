class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        frm = set()
        to = set()
        
        for x,y in paths:
            frm.add(x)
            to.add(y)
            
        
        for val in to:
            if val not in frm:
                return val
            