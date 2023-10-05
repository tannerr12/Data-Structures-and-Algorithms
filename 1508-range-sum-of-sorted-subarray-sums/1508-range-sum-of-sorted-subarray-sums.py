class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        ans = []
        for i in range(len(nums)):
            run = nums[i]
            ans.append(run)
            
            for j in range(i+1, len(nums)):
                run += nums[j]
                ans.append(run)
        
        
        ans.sort()
        
        MOD = 10 ** 9 + 7
        total = 0
        for i in range(left-1, right):
            total = (total + ans[i]) % MOD
        
        return total