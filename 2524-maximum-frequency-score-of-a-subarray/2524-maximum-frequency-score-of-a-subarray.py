class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        
        #3 1 : 1 
        #2 1, 1, 2 = 1 - (1 ** 1) = 0 + 1 ** 2 + 2 ** 1 = 3
        #3 - 1 ** 2 = 2 + (1 ** 2)
        #3 - 1 ** 2 - 2**1 = 0 + (1 ** 1) + (2 ** 2) = 5
        MOD = 10 ** 9 + 7
        res = 0
        cur = 0
        running = defaultdict(int)
        
        for i in range(len(nums)):
            
            if i < k-1:
                running[nums[i]] += 1
            elif i == k -1:
                running[nums[i]] += 1
                for key,val in running.items():
                    cur = (cur + pow(key,val,MOD)) % MOD
                    cur %= MOD
                
                res = max(res, cur)
            else:
                
                cur = (cur - pow(nums[i-k],running[nums[i-k]], MOD)) % MOD
                if nums[i] in running:
                    cur = (cur - pow(nums[i],running[nums[i]], MOD)) % MOD 
                    cur %= MOD
                
                running[nums[i-k]] -= 1
                if running[nums[i-k]] == 0:
                    del running[nums[i-k]]
                running[nums[i]] +=1
                
                if nums[i-k] in running:
                    cur = (cur + pow(nums[i-k],running[nums[i-k]], MOD)) % MOD
                cur = (cur + pow(nums[i], running[nums[i]], MOD)) % MOD 
                
                
                res = max(res, cur)
        
        
        return res
                
        
        