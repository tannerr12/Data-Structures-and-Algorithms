class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        #it either has to square in individually the source or the target
        
        #what makes a squared in?
        #we start at a point and we end at the same point eventually when bfs from the wall 
        #we start at a wall point than cycle around to hit the same wall through bfs
        
        #one of the two points must be in this square
        #if both are in this square we need to do further checks
        
        #or we can try to jump all the way until we hit a wall than ride that wall until we have a direct path in?
        bset = set()
        for x,y in blocked:
            bset.add((x,y))

        
        #jump to closest wall 
        curx,cury = source[0],source[1]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        mil = 10 ** 6
        
        def bfs(source,target):
            seen = set()

            q = deque([[source[0], source[1]]])
            seen.add((source[0],source[1]))
            for i in range(len(bset) * 2):

                for j in range(len(q)):

                    x,y = q.popleft()

                    if [x,y] == target:
                        return True

                    for a,b in directions:
                        newx,newy = x + a, y + b
                        if newx >= 0 and newx < mil and newy >= 0 and newy < mil and (newx,newy) not in bset and (newx,newy) not in seen:
                            seen.add((newx,newy))
                            q.append((newx,newy))
        
                
                if len(q) == 0:
                    return False
                elif len(q) == 20000:
                    return True


            return True
        
        return bfs(source,target) and bfs(target, source)
                
                
        