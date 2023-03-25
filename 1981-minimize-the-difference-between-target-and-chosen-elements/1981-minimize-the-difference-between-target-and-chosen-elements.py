class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        res = 0
        
        for i in range(len(mat)):
            res += mat[i][0]
            
        res = abs(target - res)
        
        @cache
        def dfs(r,total):
            nonlocal res
            if total - target >= res or res == 0:
                return
            if r == len(mat):
                res = min(res,abs(target - total))
                return 

            for j in range(len(mat[r])):
                dfs(r + 1,total + mat[r][j])
            
            return res
        
        
        return dfs(0,0)