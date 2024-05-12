class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for j in range(n-2)] for i in range(n-2)]
        
        
        print(ans)
        
        for i in range(n-2):
            for j in range(n-2):
                
                best = 0
                for ik in range(i, i+3):
                    for jk in range(j,j+3):
                        best = max(best, grid[ik][jk])
                
                ans[i][j]= best
                
        
        return ans