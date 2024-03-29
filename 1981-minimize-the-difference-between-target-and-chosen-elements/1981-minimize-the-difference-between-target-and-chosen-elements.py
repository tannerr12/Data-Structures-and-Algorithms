class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        res = 0
        #sorting is very important here and will optimize by 400% this is because we exit early if the value is too large
        #I also set our base as the smallest sum in the array to help our exit early
        for i in range(len(mat)):
            mat[i].sort()
            res += mat[i][0]
            
        res = abs(target - res)
        
        
        @cache
        def dfs(r,total):
            nonlocal res
            if total - target >= res or res == 0:
                return res
            if r == len(mat):
                res = min(res,abs(target - total))
                return res

            for j in range(len(mat[r])):
                dfs(r + 1,total + mat[r][j])
            
            return res
        
        
        return dfs(0,0)