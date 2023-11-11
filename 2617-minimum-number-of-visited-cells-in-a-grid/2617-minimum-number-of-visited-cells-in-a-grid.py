from collections import deque, defaultdict
from sortedcontainers import SortedList
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        q = deque([(0, 0)])
        rows, cols = defaultdict(lambda:SortedList()), defaultdict(lambda:SortedList())
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                rows[i].add(j)
                cols[j].add(i)
        
        level = 0
        

        while q:
            level += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                # Check if the end is reached
                if x == m - 1 and y == n - 1:
                    return level
                if (x + grid[x][y] >= m-1 and y == n-1) or (x == m - 1 and y + grid[x][y] >= n -1):
                    return level + 1
        
                l = bisect_left(rows[x], y)
                r = bisect_right(rows[x], y + grid[x][y])
                

                # Rightward movement
                remove = []
                while l < r:
             
                    q.append((x, rows[x][l]))
                    #remove.append([x, rows[x][i]])
                    rows[x].remove(rows[x][l])
                    r -= 1
                
                #for a,b in remove:
                #    rows[a].remove(b)
                
                l = bisect_left(cols[y], x)
                r = bisect_right(cols[y], x + grid[x][y])
                

                # Rightward movement
                remove = []
                while l < r:
             
                    q.append((cols[y][l], y))
                    cols[y].remove(cols[y][l])
                    r -= 1   
                
                #for a,b in remove:
                #    cols[b].remove(a)


        return -1
