class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        grid = []
        start = 0
        for i in range(len(mat)):
            ls = []
            ls.append(mat[i][0] + 0)
            for j in range(1,len(mat[0])):
                ls.append(mat[i][j] + ls[-1])
            
            grid.append(ls)
            
            #start = ls[-1]
        
        
        #print(grid)
       
        def isGood(val):
            
            for i in range(len(mat)- (val-1)):
                for j in range(len(mat[0])-(val-1)):
                    if val == 1:
                        if mat[i][j] <= 1:
                            return True
                    else: 
                        total = 0
                        for k in range(val):
                            if j == 0:
                                total += grid[i+k][j + (val-1)]
                            else:
                                total += grid[i+k][j + (val-1)] - grid[i+k][j-1]

                        if total <= threshold:
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
                
                
                