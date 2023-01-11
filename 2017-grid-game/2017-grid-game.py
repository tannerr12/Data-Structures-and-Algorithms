class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        
        prefixL = [grid[1][0]]
        postfixU = [grid[0][-1]]
        for i in range(1,len(grid[0])):
            postfixU.append(postfixU[-1] + grid[0][-(i +1)])
            prefixL.append(prefixL[-1] + grid[1][i])
        
        gap = 0
        res = float('inf')
        for i in range(len(grid[0])):
            v = grid[0][i] + grid[1][i] + (prefixL[-1] - prefixL[i]) + (postfixU[-1] - postfixU[-(i + 1)])
            v2 = max(postfixU[-(i + 1)] - grid[0][i], prefixL[i] - grid[1][i])
            if v > v2 and gap <= abs(v-v2):
                res = min(res, v2)

                
        return res