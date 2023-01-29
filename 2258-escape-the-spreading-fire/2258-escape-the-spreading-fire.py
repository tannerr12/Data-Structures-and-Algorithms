class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        #load the q with fires and person
        dq = deque()
        
        m, n = len(grid),len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    dq.append((r,c))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        
        def isGood(wait):
            q = dq.copy()
            
            #bfs each fire and person at the same time
            #if the person can reach the safehouse return True else return False
            pq = deque()
            pseen = set()
            fseen = set()
            wait +=1
            started = False
            safehouse = False
            while q or pq or not started:
                if started and len(pq) == 0 or safehouse:
                    break
                for i in range(len(q)):
                    
                    r,c = q.popleft()
                    
                    fseen.add((r,c))
                        
                    for x,y in directions:
                        nx = x + r
                        ny = y + c
                        
                        if nx >= 0 and ny >= 0 and nx < m and ny < n and grid[nx][ny] != 2 and (nx,ny) not in fseen:
                            if r == m -1 and c == n-1:
                                safehouse = True
                            fseen.add((nx,ny))
                            q.append((nx,ny))
                        
                
                if wait == 1 or (len(q) == 0 and not started):
                    pq.append((0,0))
                    wait -=1
                    started = True
                else:
                    wait = max(0, wait-1)
                
                
                if wait == 0:
                    for i in range(len(pq)):   
                        
                        r,c = pq.popleft()
                        if r == m -1 and c == n -1:
                            return True
                        if (r,c) in pseen:
                            continue
                        pseen.add((r,c))
                        
                        for x,y in directions:
                            nx = x + r
                            ny = y + c
                            if nx == m -1 and ny==n -1 and not safehouse:
                                return True
                            if nx >= 0 and ny >= 0 and nx < m and ny < n and grid[nx][ny] != 2 and (nx,ny) not in pseen and (nx,ny) not in fseen:
                                pq.append((nx,ny))
                
            return False
        
        
        #binary search minutes wait and see if we can make it or not
        #if we can search right if not search left
        
        l = 0 
        r = 10000
        res = -1
        while l <= r:
            
            mid = (l+r)//2
            
            if isGood(mid):
                res = mid
                l = mid+1
            else:
                r = mid -1
        
        
        return res if res != 10000 else 10 ** 9
                