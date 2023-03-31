class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        bitOr = 0
        
        for num in nums:
            
            bitOr |= num
            
        
        #print(bitOr)
        
        ans = set()
        
       
        def backtrack(i, mask,val):
            nonlocal bitOr
            nonlocal ans
            
            if val == bitOr and mask not in ans:
                ans.add(mask)
                
            if i >= len(nums):
                return
        
            #dont take
            backtrack(i+1, mask,val)
            
            
            #take
            if mask | (1 << i) not in ans:
                backtrack(i+1, mask | (1 << i), val | nums[i])
            
  
        
        backtrack(0,0,0)
        return len(ans)
       
        
        
        