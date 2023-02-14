class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits) -1,-1,-1):
            
            calc = digits[i] + carry
            if calc > 9:
                carry = 1
                calc = calc -10
            else:
                carry = 0
            
            
            digits[i] = calc
        
        
        if carry:
            digits = [carry] + digits
        return digits
            
            
            