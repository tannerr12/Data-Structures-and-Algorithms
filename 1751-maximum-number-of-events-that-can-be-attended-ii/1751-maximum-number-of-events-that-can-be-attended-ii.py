class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        dayGroups = defaultdict(list)
        mx = 0
        for i in range(len(events)):
            events[i][0] -=1
            dayGroups[events[i][0]].append([events[i][1], events[i][2]])
            mx = max(mx,events[i][0])
            
        days = list(dayGroups)

        @cache
        def dfs(day,k):
           
            if day >= len(days) or k == 0:
                return 0
            didx = day
            day = days[day]
            res = 0
            #goto next event
            for end, val in dayGroups[day]:
                b = bisect_left(days,end)
                res = max(res, dfs(b, k-1) + val)
            
            #skip it 
            res = max(res, dfs(didx + 1, k))
            
            
            return res
        
        return dfs(0, k)
            