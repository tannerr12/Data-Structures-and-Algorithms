class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        """
        directions = [[-2,-1], [-2,1], [-1, 2], [1,2], [2,1], [2,-1], [1,-2],[-1,-2]]
        grid = [[0 for j in range(3)] for i in range(4)]
        count =1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = count
                count +=1
        
        grid[-1][0]= -1
        grid[-1][-1] = -1
        grid[-1][1] = 0
        
        print(grid)
        """
        mp = {0: [4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4: [9,3,0], 5: [], 6: [0,7,1], 7: [6,2], 8:[1,3], 9:[4,2]}
        # 1 -> 6, 8
        # 2 -> 7,9
        # 3 -> 4, 8
        # 4 -> 9, 3, 0
        # 5 is a dead end
        # 6 -> 0, 7, 1
        #7 -> 6,2
        # 8 -> 1,3
        # 9 -> 4,2
        # 0 -> 4,6
        
        @cache
        def dfs(cur, rem):
            
            if rem == 0:
                return 1
            
            res = 0
            for adj in mp[cur]:
                
                res += dfs(adj,rem-1) % MOD
            
            
            return res
        
        res = 0
        
        for i in range(10):
            res += dfs(i,n-1)
        
        
        return res % MOD