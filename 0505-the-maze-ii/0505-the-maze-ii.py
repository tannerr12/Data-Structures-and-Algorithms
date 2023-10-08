class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        q = deque()
        sr,sc = start
        q.append((sr,sc,0))
        seen = {}
        res = float('inf')

        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while q:
           
            x,y,steps = q.popleft()

            if steps >= res:
                continue
            if [x,y] == destination:
                res = min(res,steps)
                

            for a,b in directions:
                tempr,tempc = x+a,y+b
                dist = 0
                while tempr >= 0 and tempr < len(maze) and tempc >= 0 and tempc < len(maze[0]) and maze[tempr][tempc] != 1:
                    tempr += a
                    tempc += b
                    dist +=1
                    
                if [tempr -a,tempc - b] != [x,y] and ((tempr-a,tempc-b) not in seen or steps + dist < seen[(tempr-a,tempc-b)]):
                    seen[(tempr-a,tempc-b)] = steps + dist
                    q.append((tempr-a,tempc-b, steps + dist)) 
                

        return res if res != float('inf') else -1
