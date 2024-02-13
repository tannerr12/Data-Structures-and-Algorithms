class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        
        for i in range(len(queries)):
            queries[i] = [queries[i][0], queries[i][1], i]
        
        queries.sort()
        
        mp = defaultdict(lambda:defaultdict(int))
        
        for i in range(len(nums)):
            mp[i] = mp[i-1].copy()
            mp[i][nums[i]] += 1
        
        
        #print(mp)
        ans = [-1] * len(queries) 
        for i in range(len(queries)):
            l,r,idx = queries[i]
            
            diff = float('inf')
            last = float('-inf')
            for i in range(1, 101):
                if i in mp[r] and mp[r][i] - mp[l-1][i] > 0 and last != i:
                    diff = min(diff, i - last)
                    last = i
                    
            
            ans[idx] = diff if diff != float('inf') else -1
        
        return ans
            