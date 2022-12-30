# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
    
        row,col = binaryMatrix.dimensions()
        
        
        
        def binarySearch(row,col):
            
            l,r = 0, col-1
            
            while l <= r:
                
                curr = (l+r) // 2
                val = binaryMatrix.get(row,curr)
                
                if (val == 1 and curr == 0) or (val == 1 and binaryMatrix.get(row,curr -1) == 0):
                    
                    return curr
                    
                elif val == 1:
                    r = curr -1
                
                else:
                    l = curr +1
                
                
            return float('inf')
        
        res = float('inf')

        for r in range(row):
            
            #if binaryMatrix.get(r, col-1) == 0:
             #   continue
            
            
            res = min(binarySearch(r,col), res)
            
        
        
        
        return res if res != float('inf') else -1
        
            
            