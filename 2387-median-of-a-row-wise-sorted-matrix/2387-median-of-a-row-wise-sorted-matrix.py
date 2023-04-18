class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        
        midGrid = (len(grid) * len(grid[0])) //2
        
        
        def isGood(mid):
            count = 0
            for i in range(len(grid)):
                
                count += bisect_right(grid[i], mid)
            
            return count > midGrid
        
        l,r = 0,10 ** 6
        res = 0
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                
                res = mid
                r = mid - 1
                
            else:
                l = mid + 1
        
        
        
        return res