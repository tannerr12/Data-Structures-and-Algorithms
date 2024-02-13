class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
                
        mp = defaultdict(lambda:defaultdict(int))
        
        for i in range(len(nums)):
            mp[i] = mp[i-1].copy()
            mp[i][nums[i]] += 1
        
        ans = [-1] * len(queries) 
        for j in range(len(queries)):
            l,r = queries[j]
            
            diff = float('inf')
            last = float('-inf')
            for i in range(1, 101):
                if i in mp[r] and mp[r][i] - mp[l-1][i] > 0 and last != i:
                    diff = min(diff, i - last)
                    last = i
                    
            
            queries[j] = diff if diff != float('inf') else -1
        
        return queries
            