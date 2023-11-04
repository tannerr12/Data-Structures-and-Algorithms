class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        
        #1,1,2,2,1,1
        #0,0,    2,2
        mp = defaultdict(list)
        mpIdx = defaultdict(int)
        for i in range(len(nums)):
            if len(mp[nums[i]]) == 0:
                mp[nums[i]].append((0, i))
            else:
                mp[nums[i]].append((mp[nums[i]][-1][0] + (i - mp[nums[i]][-1][1] - 1), i))
            
    
        #print(mp)
        res = 0
        
        for i in range(len(nums)):
            
            idx = bisect_right(mp[nums[i]], mp[nums[i]][mpIdx[nums[i]]][0] + k, key=lambda x:x[0])
            res = max(res, idx - mpIdx[nums[i]])
            mpIdx[nums[i]] += 1
        
        
        return res
            