class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        
        res = 0
        
        
        
        def dfs(r,c):
            
            if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0 or board[r][c] == ".":
                return 
            
            
            board[r][c] = "."            
            #check right 
            dfs(r,c+1)
            
            #check down
            dfs(r+1,c)
            
                
            
        for r in range(len(board)):
            
            for c in range(len(board[0])):
               
                if board[r][c] == "X":
                    dfs(r,c)
                    res +=1
        
        
        return res