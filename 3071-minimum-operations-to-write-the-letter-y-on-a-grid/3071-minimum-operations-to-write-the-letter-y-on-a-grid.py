class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        mid = len(grid) // 2
        n = len(grid)
        y = defaultdict(int)
        al = defaultdict(int)
        countY = 0
        for i in range(n):
            for j in range(n):
                al[grid[i][j]] += 1
        
        for i in range(mid):
            y[grid[i][i]] += 1
            y[grid[i][n-i-1]] += 1
            al[grid[i][i]] -=1
            al[grid[i][n-i-1]] -=1
            countY+=1
        for i in range(mid, len(grid)):
            y[grid[i][mid]] += 1
            al[grid[i][mid]] -=1
            countY+=1
        #print(y)
        #print(al)
        other = (n * n) - countY
        res = float('inf')
        #y
        for i in range(3):
            cost = countY - y[i]
            #other  
            for j in range(3):
                if i == j:
                    continue
                res = min(res, cost + (other - al[j]))
        
        
        return res
        