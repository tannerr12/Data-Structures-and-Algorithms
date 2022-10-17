class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
       
        

        column = len(board)
        row = len(board[0])
        for c in range(column ):
            for r in range(row ):
                cell = board[c][r]
                
                if cell.isdigit():
                    #result = scan(board,c,r,cell)
                    if cell in rows[r]:
                        return False
                    rows[r].add(cell)
                    
                    if cell in cols[c]:
                        return False
                    cols[c].add(cell)
                    
                    #check box
     
                    idx = (r//3) *3 + c//3
                    if cell in boxes[idx]:
                        return False
                    boxes[idx].add(cell)
                    
        
        
        
        
        
        
        
        return True