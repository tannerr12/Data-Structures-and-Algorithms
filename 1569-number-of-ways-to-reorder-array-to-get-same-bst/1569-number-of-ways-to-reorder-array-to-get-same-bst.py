class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
    
        def dfs(arr):
            
            if len(arr) < 3:
                return 1
            res = 0
            l = []
            r = []
            for num in arr:
                if num < arr[0]:
                    l.append(num)
                elif num > arr[0]:
                    r.append(num)
        
            left = dfs(l)
            right = dfs(r)
            
            return left * right * comb(len(arr) -1, len(l)) % MOD
        
        
        return (dfs(nums) -1) % MOD