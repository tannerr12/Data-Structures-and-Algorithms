class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        
        total =0
        
        for num in nums:
            
            if num % 2 == 0:
                
                total += num
                
            
        
        res = []
        for i in range(len(queries)):
            
            val,idx = queries[i]
            
            even = False
            
            if nums[idx] % 2 == 0:
                even = True
            
            tempsum = nums[idx] + val
            
            if not even and tempsum % 2 ==0:
                total += tempsum
            if even and tempsum %2 ==1:
                total -= nums[idx]
            
            if even and tempsum % 2 == 0:
                total += val
                
            
            
            res.append(total)
            nums[idx]= tempsum
        
        
        return res
            
            
                