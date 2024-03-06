class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        k = len(days[0])
        

        
        #100 weeks 100 possible flights
        
        @cache
        def dfs(week, location):
            
            if week == k:
                return 0
            
            res = 0
            for i,loc in enumerate(flights[location]):
                if loc == 0:
                    continue
                res = max(res, dfs(week+1, i) + days[i][week])
            
            #stay
            res = max(res, dfs(week+1, location) + days[location][week])
            
            return res
        
        
        return dfs(0,0)
    