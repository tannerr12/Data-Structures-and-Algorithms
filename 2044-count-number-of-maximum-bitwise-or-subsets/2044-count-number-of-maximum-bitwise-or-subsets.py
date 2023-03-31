class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        

        
        mp = defaultdict(int)
        mp[0] = 1
        
        for i in range(len(nums)):
            for k,c in list(mp.items()):    
                mp[k | nums[i]] += c
        
        
        return mp[max(mp)]
        """
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
            backtrack(i+1, mask | (1 << i), val | nums[i])
            
  
        
        backtrack(0,0,0)
        return len(ans)
       
        
        
        """