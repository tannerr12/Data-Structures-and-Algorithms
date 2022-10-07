class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [[1,1],[1,0],[0,1],[-1,-1],[-1,0],[0,-1],[1,-1],[-1,1]]
       # while True:
            
        tempBoard = deepcopy(board)
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                    
                count = 0
                    
                dead = False
                if board[i][j] == 0:
                    dead = True
                    #check 8 dir 
                for x,y in directions:
                    if i + x < 0 or i + x >= len(board) or j + y < 0 or j + y >= len(board[0]):
                            continue
                        
                    if board[x+i][y+j] == 1:
                        count +=1
                    
                    
                if (count == 3 or count == 2 and not dead) or (dead and count == 3): 
                    tempBoard[i][j] = 1
                    
                    
                else:
                    tempBoard[i][j] = 0
                
            
                
                
#if tempBoard == board:
                  #  break
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                board[i][j] = tempBoard[i][j]