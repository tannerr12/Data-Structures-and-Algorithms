class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        """
        s = set()
        
        @cache
        def dfs(i,curr):
            s.add(curr)
            if i >= len(nums):
                return
            
            if nums[i] > curr:
                #take 
                dfs(i+1, gcd(curr,nums[i]))
            #dont take
            dfs(i+1,curr)
            
            return 
        
        dfs(0,0)
        #print(s)
        return len(s) -1
        """
        
        
        nset = set(nums)
        
        mx = max(nums)
        
        res = 0
        
        for i in range(1, mx + 1):
            currGcd = 0
            for j in range(i, mx + 1, i):
                
                if j in nset:
                    currGcd = gcd(currGcd, j)
                    
                    if currGcd == i:
                        res +=1
                        break
                    if currGcd < i:
                        break
        
        return res
            
        