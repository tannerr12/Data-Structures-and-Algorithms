class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        m = defaultdict(list)
        nums.sort()
        
        for v in nums:
            flag = False
            for val in m:
                if v - m[val][-1] == k:
                    m[val].append(v)
                    flag = True
            if not flag:
                m[v] = [v]
        
        def dfs(ls):
            n = len(ls)
            if n == 1:
                return 2
            
            dp = [0] * (n + 1)
            dp[0] = 1
            dp[1] = 2
            
            for i in range(2, n + 1):
                dp[i] = dp[i-1] + dp[i-2]
            
            return dp[-1]
        
        res = 1
        for val in m:
            res *= dfs(m[val])
        
        return res