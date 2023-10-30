class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:



        directionsUp = [[-1,-2], [-2,-1], [-2,1], [-1,2]]
        directionsDown = [[1,-2], [2,-1], [2,1], [1,2]]
        q = deque()
        q.append([0,0])
        level = 0
        seen = set()
        while q:

            for i in range(len(q)):

                r,c = q.popleft()

                if (r,c) in seen:
                    continue
                seen.add((r,c))
                
                if r == y and c == x:
                    return level
            
                if r > y:
                    for a,b in directionsUp:
                        if (r+a,c+b) in seen:
                            continue
                        q.append([r+a,c+b])
                else:
                    for a,b in directionsDown:
                        if (r+a,c+b) in seen:
                            continue
                        q.append([r+a,c+b])

            level +=1
        

        return 0