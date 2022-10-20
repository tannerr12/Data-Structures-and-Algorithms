class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        

        shift = 0
        
        
        
        while right > left:
            
            
            right = right >> 1
            
            left = left >> 1
            
            shift +=1
            
        
        
        return right << shift