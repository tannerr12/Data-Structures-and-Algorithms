class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        
        
        res = 0
        maxEndHere = 0
        maxEndOneSquare = 0
        
        for n in nums:
            
            #find best squared and non squared
            maxEndOneSquare = max(maxEndHere + n * n, maxEndOneSquare + n)
            
            maxEndHere = max(0, maxEndHere + n)
            
            res = max(res, maxEndOneSquare, maxEndHere)
            
        
        return res
            
            