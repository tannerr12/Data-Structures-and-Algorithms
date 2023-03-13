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
        
        dp = [{} for _ in nums]
        mx = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                if diff in dp[i]:
                    dp[j][diff] = dp[i][diff] + 1
                else:
                    dp[j][diff] = 1
                
                mx = max(mx, dp[j][diff])
        
        return mx + 1 if mx > 0 else 0
        
        
        
        