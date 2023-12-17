class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks = sorted(tasks, key=lambda x: (-(x[1] - x[0])))
              
        #[[10, 12], [10, 11], [8, 9], [2, 4], [1, 3]]
        #31        29    19       9      1
        #[[1,3],[2,4],[10,11],[10,12],[8,9]]
        #print(tasks)
        def isGood(energy):
            
            for x,y in tasks:
                if energy < y or energy < x:
                    return False
                energy -= x
            
            return True
        
        l,r = 0, 10 ** 9
        res = 0
        while l <= r:
            
            mid = (l+r) // 2
            
            if isGood(mid):
                res = mid
                r = mid-1
                
            else:
                l = mid+1
                
            
        
        return res