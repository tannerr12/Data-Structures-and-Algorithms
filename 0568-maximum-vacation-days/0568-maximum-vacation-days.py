class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        k = len(days[0])
        
        adj = defaultdict(list)
        
        for i in range(len(flights)):
            for j in range(len(flights[i])):
                if flights[i][j] > 0:
                    adj[i].append(j)
        
        #print(adj)
        
        #bfs 100 ** 100
        
        #100 weeks 100 possible flights
        
        @cache
        def dfs(week, location):
            
            if week == k:
                return 0
            
            res = 0
            for loc in adj[location]:
                res = max(res, dfs(week+1, loc) + days[loc][week])
            
            #stay
            res = max(res, dfs(week+1, location) + days[location][week])
            
            return res
        
        
        return dfs(0,0)
    