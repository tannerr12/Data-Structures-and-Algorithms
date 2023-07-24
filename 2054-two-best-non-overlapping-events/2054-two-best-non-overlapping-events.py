class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        vals = []
        events.sort()
        mx = 0
        idx = 0
        for i in range(len(events)-1,-1,-1):
            mx = max(mx,events[i][2])
            vals.append((events[i][0], mx))
            
        vals = vals[::-1]
        
        #print(vals)
        
        
        res = 0
        
        for i in range(len(events)):
            
            left = events[i][2]
            right = bisect_left(vals, events[i][1] + 1, key = lambda x:x[0])
            
            if right < len(vals):
                res = max(res, left + vals[right][1])
            else:
                res = max(res, left)
        
        return res