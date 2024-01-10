class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        
        c = Counter(nums)
        stack = []
        left = []
        i = 0
        
        while i < len(nums):
            c[nums[i]] -= 1
            if c[nums[i]] > 0:
                stack.append(nums[i])
            while stack and c[stack[-1]] == 0:
                stack.pop()
            if len(stack) == 0:
                left.append(i)
            
            i+=1
        
        #print(left)
            
        
        #1 * 3 = 3
        #2 * 2 = 4
        #3 * 1 = 3
       
    
        #1,2,3,4
        #4 + 2 + 1 + 1
        #1, 2, 3, 4
        #1,23,4
        #1,234
        #1,2,34
        
        #12, 3, 4
        #12,34
        
        #123,4
        
        #1234

        
        #123,4
        
        MOD = 10 ** 9 + 7
        return pow(2,len(left) -1, MOD)
        '''
        @cache
        def dfs(i):
            
            if i >= len(left):
                return 1
            
            res= 0
            #for j in range(1, len(left) - i + 1):
            res += dfs(i+1) * ((len(left) - i) - 1)
            res %= MOD
            
            return res % MOD
        
        return dfs(0)
        
        '''