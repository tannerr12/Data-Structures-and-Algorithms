class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:

        MOD = 10 ** 9 + 7

        #print(newnums)
        
        @lru_cache(maxsize=50000)
        def dfs(i,cur):
            
            if i >= len(nums):
                return cur == 2
            
            res = 0
            #take number and increase
            if nums[i] == cur + 1:
                res += dfs(i+1, cur+1) % MOD
                res %= MOD
                #take number or skip
                res += ((dfs(i+1,cur) % MOD) * 2) % MOD
            else:
                res += dfs(i+1, cur) % MOD
                
            return res % MOD
            
        
        return dfs(0,-1)