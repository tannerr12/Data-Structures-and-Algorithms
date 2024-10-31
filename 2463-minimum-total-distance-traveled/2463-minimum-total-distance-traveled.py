class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @cache
        def dfs(i,j,k):
            
            if i >= len(robot):
                return 0
            if j>= len(factory):
                return float('inf')
            
            res = float('inf')
            res2 = float('inf')
            if factory[j][1] > k:
                
                res = min(res, dfs(i+1,j,k+1) + abs(robot[i] - factory[j][0]))
               
            
            res2 = min(res2, dfs(i,j+1,0))
            
            return min(res,res2)
        
        
        return dfs(0,0,0)