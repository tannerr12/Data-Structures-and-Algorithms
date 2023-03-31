class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        """
        #count occurances of each xor and add them to the new xor when a new number allows it to reach
        mp = defaultdict(int)
        mp[0] = 1
        
        for i in range(len(nums)):
            for k,c in list(mp.items()):    
                mp[k | nums[i]] += c
        
        
        return mp[max(mp)]
        
        ans = set()
        
        """
        bitOr = 0
        for num in nums:
            bitOr |= num
            
        
        def backtrack(i, mask,val):
            nonlocal bitOr
            #nonlocal ans
            
            if i >= len(nums):
                if val == bitOr:
                    return 1
                return 0
        
            res = 0
            #dont take
            res += backtrack(i+1, mask,val)
            
            
            #take
            res += backtrack(i+1, mask | (1 << i), val | nums[i])
            
            return res
        
        return backtrack(0,0,0)
        
       
        
        
        