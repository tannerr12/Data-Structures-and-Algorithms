class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        
        count = 0
        mp = defaultdict(int)
        total = 0
        res = 0
        
        for i in range(len(nums)):
            
            
            mp[nums[i]] += 1
            
            #if mp[nums[i]] == 2:
            #    count -=1
            if mp[nums[i]] == 1:
                count += 1
            total += nums[i]
            
            if i - k >= 0:
                mp[nums[i-k]] -= 1
                if mp[nums[i-k]] == 0:
                    count -= 1
                #elif mp[nums[i-k]] == 1:
                #    count += 1
                total -= nums[i-k]
                
            
            if count >= m and i >= k-1:
                res = max(res, total)
                
        
        return res
            
            
                