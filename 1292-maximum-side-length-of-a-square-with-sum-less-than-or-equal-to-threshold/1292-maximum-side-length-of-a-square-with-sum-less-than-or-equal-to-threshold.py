class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        grid = [[0 for j in range(len(mat[0]) +1)] for i in range(len(mat) +1)]
        
        start = 0
        for i in range(len(grid) -2,-1,-1):
            for j in range(len(grid[0]) -2,-1,-1):
                grid[i][j] = mat[i][j] + grid[i+1][j] + grid[i][j+1] - grid[i+1][j+1]
                
        
        
        #print(grid)
        print(grid)
        def isGood(val):
            
            for i in range(len(mat)- (val-1)):
                for j in range(len(mat[0])-(val-1)):
                    if (grid[i][j] - grid[i + val][j] - grid[i][j + val]) + grid[i+val][j+val] <= threshold:
                        return True
                
            
            return False
        
        l,r = 1,min(len(mat), len(mat[0]))
        res = 0
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                l = mid +1
                res = mid
                
            else:
                r = mid -1
        
        return res
                
                
                