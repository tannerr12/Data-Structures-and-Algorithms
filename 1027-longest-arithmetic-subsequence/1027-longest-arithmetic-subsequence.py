class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
       
        """
        memo = {}
        def dfs(i,seq,last,s):
            
            if i >= len(nums):
                return 0
            
           
            res = 0
            if (i,seq) in memo:
                return memo[(i,seq)]
            #take
            if last + seq == nums[i] or seq == float('inf'):
                val = nums[i] - last
                if last == float('inf'):
                    val = float('inf')
                res = max(res,dfs(i+1, val,nums[i], s + ',' + str(nums[i])) +1)
                
            #dont take
            if last + seq != nums[i]:
                res = max(res, dfs(i+1, seq, last,s))
            
            memo[(i,seq)] = res
            return res
        
        return dfs(0,float('inf'), float('inf'),'')
        """
        
        #very tricky, top down dp does not work there is no way to memoize the information properly instead we use bottom up dp with an array of hashmaps
        #the idea is that if we see a sequence we can update our current j to be dp[i][diff] + 1 and we keep track of the max value seen
       
        dp = [{} for _ in nums]
        mx = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if diff in dp[i]:
                    dp[j][diff] = dp[i][diff] + 1
                else:
                    dp[j][diff] = 2
                
                mx = max(mx, dp[j][diff])
        
        return mx 
        
        
        
        