class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
                
        mp = defaultdict(lambda:defaultdict(int))
        
        for i in range(len(nums)):
            mp[i] = mp[i-1].copy()
            mp[i][nums[i]] += 1
        
        ans = [-1] * len(queries) 
        for j in range(len(queries)):
            l,r = queries[j]
            c = r - l + 1
            diff = float('inf')
            last = float('-inf')
            for i in range(1, 101):
                if i in mp[r] and mp[r][i] - mp[l-1][i] > 0:
                    if last != i:
                        diff = min(diff, i - last)
                        last = i
                    else:
                        c -= 1
                        if c == 0:
                            break
                    
            
            queries[j] = diff if diff != float('inf') else -1
        
        return queries
            