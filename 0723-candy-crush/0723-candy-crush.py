class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        localSeen = set()
    
        def dfs(i,j,d,target):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] != target or (i,j) in localSeen or board[i][j] == 0:
                return 0
            
            localSeen.add((i,j))
            
            if d == 'v':
                dfs(i+1,j,d,target)
                dfs(i-1,j,d,target)
            else:
                dfs(i,j+1,d,target)
                dfs(i,j-1,d,target)
            
            
        while True:
            colshift = defaultdict(int)
            poplist = set()
            for i in range(len(board)):

                for j in range(len(board[0])):

                    dfs(i,j,'v',board[i][j])
                    if len(localSeen) > 2:
                        poplist.update(localSeen)
                    localSeen = set()
                    dfs(i,j,'h', board[i][j])
                    if len(localSeen) > 2:
                        poplist.update(localSeen)

                    localSeen = set()
            
            if len(poplist) == 0:
                return board
            h = defaultdict(list)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if (i,j) in poplist:
                        continue
                    h[j].append(board[i][j])
            #print(h)

            for i in range(len(board) -1,-1,-1):
                for j in range(len(board[0])-1,-1,-1):

                    if h[j]:
                        val = h[j].pop()
                        board[i][j] = val
                    else:
                        board[i][j] = 0


                    

            #print(board)
        
        
                
                
        
                