class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        
        andVal = 0
        
        
        for val in arr2:
            andVal ^= val
        
        res = 0
        for val in arr1:
            res ^= val & andVal

        
        return res

        
        