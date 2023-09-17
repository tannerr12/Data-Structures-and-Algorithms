class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        
        bitmask = 0
        andVal = 0
        
        arr = []
        for val in arr2:
            andVal ^= val
        
        for val in arr1:
            arr.append(val & andVal)
            
        
        res = 0
        
        for val in arr:
            res ^= val
        
        return res

        '''
        001
        110
        101
        
    
        000
        001
        010
        000
        010
        011
        010
        
        
        001
        010
        011
        
        000
        
        
        
        110
        101
        
        
        010
        011
        
        011
        011
        111
        
        001
        010
        011
        000
        
        
        001
        
        011
        
        '''
        
        