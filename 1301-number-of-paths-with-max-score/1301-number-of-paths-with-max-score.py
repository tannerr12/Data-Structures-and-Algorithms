class Solution:
    def pathsWithMaxScore(self, oldboard: List[str]) -> List[int]:
        MOD = 10 ** 9+ 7
        n,m = len(oldboard), len(oldboard[0])
        board = [[0 for j in range(m)] for i in range(n)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 and j == 0:
                    board[i][j] = 'E'
                    continue
                elif i == len(board) - 1 and j == len(board[0]) - 1:
                    board[i][j] = 'S'
                    continue
                elif oldboard[i][j] == 'X':
                    board[i][j] = 'X'
                    continue
                    
                board[i][j] = int(oldboard[i][j]) % MOD
        
        #print(board)
        #find the maximum sum 
        ans = [0,0]
        
        cache2 = {}
        
        def findBest(i, j):
            
            if i < 0 or j < 0 or board[i][j] == 'X':
                return float('-inf')
            
            elif (i,j) in cache2:
                return cache2[(i,j)]
            
            elif i == 0 and j == 0:
                return 0
            
            val = board[i][j] if board[i][j] != 'S' else 0
            
            res = float('-inf')
            #go left
            res = max(res, findBest(i, j-1) + val) 
            #go up
            res = max(res, findBest(i-1, j) + val) 
            #both
            res = max(res, findBest(i-1,j-1) + val) 
            
            cache2[(i,j)] = res
            
            return res 
        
        
        v1 = findBest(n-1, m-1)
        ans[0] = v1 if v1 != float('-inf') else 0
        #using the maximum sum find the count
        #print(ans)
        #print(cache)
        
        
        @cache
        def findPaths(i,j,score):
            
            if i < 0 or j < 0 or board[i][j] == 'X':
                return 0
            
            elif i == 0 and j == 0:
                return 1
            
            elif score > cache2[(i,j)]:
                return 0
            
            val = int(board[i][j]) % MOD if board[i][j] != 'S' else 0
            upleft = 0
            #go left
            left = findPaths(i, j-1,score - val) % MOD
            #go up
            up = findPaths(i-1, j,score - val) % MOD
            #both
            if up == 0 and left == 0:
                upleft = findPaths(i-1,j-1,score - val) % MOD
            
            
            
            return (left + up + upleft) % MOD
        
        ans[1] = findPaths(len(board) - 1, len(board[0]) - 1, ans[0])
        
        return ans