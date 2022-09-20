class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        newNums = nums
        
        
        
        while len(newNums) > 1:
            
            dist = len(newNums)
            for i in range(dist -1): 
                newNums[i] = (newNums[i] + newNums[i+1]) % 10
            
            newNums = newNums[:-1]
        
        
        return newNums[0]
            