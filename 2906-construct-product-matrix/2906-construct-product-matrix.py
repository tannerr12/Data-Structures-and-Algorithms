class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        
        pref = []
        pref.append(1)
        suf = []
        suf.append(1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                pref.append((pref[-1] * (grid[i][j]) % MOD))
        
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                suf.append((suf[-1] * grid[i][j]) % MOD)
        
        
        ans = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        suf = suf[::-1]
        idx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                ans[i][j] = (pref[idx] * suf[idx+1]) % MOD
                idx +=1
        return ans