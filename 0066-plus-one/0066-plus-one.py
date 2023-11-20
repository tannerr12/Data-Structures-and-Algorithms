class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        idx = len(digits)-1
        
        while idx >= 0 and digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
            
        
        if idx < 0:
            return [1] + digits
        
        else:
            digits[idx] += 1
            return digits
            
            
            