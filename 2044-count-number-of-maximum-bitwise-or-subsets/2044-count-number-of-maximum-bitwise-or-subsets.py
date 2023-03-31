class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        bitOr = 0
        
        for num in nums:
            
            bitOr |= num
            
        
        #print(bitOr)
        
        ans = set()
        
        @cache
        def backtrack(i, mask,val,tot):
            nonlocal bitOr
            nonlocal ans
            
            if val == bitOr and mask not in ans:
                ans.add(mask)
                
            if i >= len(nums):
                return tot
        
            
            res = 0
            #dont take
            res += backtrack(i+1, mask,val,tot)
            
            
            #take
            res += backtrack(i+1, mask | (1 << i), val | nums[i],tot)
            
            return res
        
        backtrack(0,0,0,0)
        return len(ans)
       
        
        
        