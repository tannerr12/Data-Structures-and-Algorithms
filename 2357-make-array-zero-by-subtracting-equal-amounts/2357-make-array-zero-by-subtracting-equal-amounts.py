class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        m = float('inf')
        
        
        for num in nums:
            
            if num >= 1 and num < m:
                m = num
                
            
        if m == float('inf'):
            return 0
        res = 0
        newM = float('inf')
        while newM == float('inf'):
            for i in range(len(nums)):
                if nums[i] - m < 0:
                    nums[i] = 0
                else:
                    nums[i] = nums[i] - m 
                if nums[i] > 0:
                    newM = min(nums[i], newM)
            
            
            res +=1
            if newM == float('inf'):
                break
                
            m = newM
            newM = float('inf')
        
            
        
            
        
        return res