class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        def checkWall(i,j):
            if i < 0 or j < 0 or i >= len(room) or j >= len(room[0]) or room[i][j] == 1:
                return True
            
            return False
            
        directions = ['R','D','L','U']
        direcVal = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque()
        q.append([0,0,0])
        cleaned = 0
        seen = set()
        while q:
            
            i,j,direc = q.popleft()
            
            if (i,j,direc) in seen:
                return cleaned
            
            if room[i][j] == 0:
                room[i][j] = 2
                cleaned += 1
            
            seen.add((i,j,direc))
            checked = 0
            while checkWall(i + direcVal[direc][0], j + direcVal[direc][1]):
                direc = (direc + 1) % len(directions)
                checked += 1
                if checked >= 4:
                    return cleaned
            q.append([i + direcVal[direc][0], j + direcVal[direc][1], direc])
            
            
        
        return -1
                
            
            
            