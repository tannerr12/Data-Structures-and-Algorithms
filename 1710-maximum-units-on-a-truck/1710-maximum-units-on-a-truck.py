class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
      
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        
        
        res = 0 
        for box,unit in boxTypes:
            
            if box <= truckSize:
                res += box * unit
                truckSize -= box 
            
            else:
                
                
                res += truckSize * unit
                truckSize = 0 
            
            
            if truckSize == 0:
                break
        
        
        return res
        
        