class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        grid =[]
        count = 0
        for i in range(len(board)-1,-1,-1):
            
            if count % 2 == 0:
            
                for j in range(len(board[0])):

                    grid.append(board[i][j])
            else:
                for j in range(len(board[0])-1,-1,-1):

                    grid.append(board[i][j])
            
            count +=1

        
        heap = [(0,0)]
        seen = set()
        
        while heap:
            
            
            val,pos = heappop(heap)
            
            if pos in seen:
                continue
            if pos == len(grid)-1:
                return val
            
            seen.add(pos)
            for i in range(1,7):
                
                if i + pos < len(grid):
                    diff = i + pos
                    
                    if grid[diff] != -1:
                        diff = grid[diff] -1
                        
                    if diff in seen:
                        continue
                    heappush(heap, (val + 1, diff))
                
                
                
            
        
        return -1