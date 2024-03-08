class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        #there would never be a reason to use 2 different tires except for the last section to be more percise
        #get the best result from each tire
        
     
        costMp = defaultdict(lambda:float('inf'))
        
        for i in range(len(tires)):
            
            x,y = tires[i]
            total = 0
            for j in range(15):
                cost = x * (y**j)
                total += cost
                costMp[j+1] = min(costMp[j+1], total)
            
          
        @cache
        def dfs(rem):
            
            if rem == 0:
                return -changeTime
        
            res = float('inf')
            
            for j in range(min(15, rem)):
                res = min(res, dfs(rem - j - 1) + costMp[j+1] + changeTime)
                
            return res
        return dfs(numLaps)