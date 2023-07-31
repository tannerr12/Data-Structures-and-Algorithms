class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        prefix = []
        prefix.append(0)
        
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
            
        
        #print(prefix)
        mp = defaultdict(list)
        for i in range(len(prefix)):
            mp[prefix[i]].append(i)
        
        '''
        #print(mp)
        def dfs(i):
                
            if i >= len(prefix):
                return 0
            res = 0
            #skip i
            res = max(res,dfs(i+1))
            
            #jump to next target + 1 and add 1
            t = prefix[i] + target
            
            if len(mp[t]) > 0:
                idx = bisect_left(mp[t], i)
                if idx < len(mp[t]):
                    res = max(res, dfs(mp[t][idx] + 1) + 1)
            
            return res
    
        return dfs(0)
        
        '''
        
        overlaps = []
        
        for i in range(len(prefix)):
            #jump to next target + 1 and add 1
            t = prefix[i] - target
            t = target + prefix[i]
            #0,-1,2,7,8,12,14,5
            if len(mp[t]) > 0:
                idx = bisect_left(mp[t], i)
                if idx < len(mp[t]):
                    if mp[t][idx] == i:
                        idx +=1
                    if idx < len(mp[t]):
                        overlaps.append([i, mp[t][idx] -1])
        #print(overlaps)
        #print(len(overlaps))
        overlaps.sort(key=lambda x:(x[1]))
        
        #print(overlaps)
        
        def dfs(i, last):
            
            if i >= len(overlaps):
                return 0
            res = 0
            #take current
            if overlaps[i][0] > last:
                res = max(res, dfs(i+1, overlaps[i][1]) + 1)
            
            #skip
            res = max(res, dfs(i+1, last))
        
            return res
        #return dfs(0,-1)
        
        res = 0
        last = -1
        for i in range(len(overlaps)):
            if overlaps[i][0] > last:
                res += 1
                last = overlaps[i][1]
        
        return res