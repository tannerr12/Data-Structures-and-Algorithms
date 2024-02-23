class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        print(len(nums))
        right = defaultdict(lambda:[0,0])
        MOD = 10 ** 9 + 7
        one,two = 0,0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 2:
                two += 1
            elif nums[i] == 1:
                one += 1
            right[i] = [one,two]
            

        powers = []
        
        for i in range(100000):
            powers.append(pow(2, i, MOD) -1)
        
        #print(right)
        
        @cache
        def dfs(i,cur):
            if i >= len(nums):
                return 0
            elif cur == 2:
                return (powers[right[i][1]]) % MOD
            
            res = 0
            #take number
            if nums[i] == cur:
                res += dfs(i+1, cur+1) % MOD
                res %= MOD
                #increase target
                res += dfs(i+1, cur) % MOD
                res %= MOD
            #skip number
            res += dfs(i+1,cur) % MOD
            
            return res % MOD
            
        
        return dfs(0, 0)