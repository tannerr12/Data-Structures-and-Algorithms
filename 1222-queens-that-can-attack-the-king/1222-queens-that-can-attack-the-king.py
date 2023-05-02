class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        
        #try all 8 directions from the king and exit once we hit a queen
        
        result = []
        q = set()
        for i in range(len(queens)):
            x,y = queens[i]
            q.add((x,y))
            
        directions = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [-1,1], [1, -1], [1, 1]]
        i,j = king[0],king[1]
        for x,y in directions:
            
            nx,ny = i + x, j + y
            while nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
                if (nx,ny) in q:
                    result.append([nx,ny])
                    break
                
                nx += x
                ny += y
        
        
        return result
        