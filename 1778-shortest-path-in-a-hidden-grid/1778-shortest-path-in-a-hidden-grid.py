# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
    
        oppMap = {'U':'D', 'D':'U','L':'R', 'R':'L'}
        ijMap = {'U':[-1,0], 'D':[1,0],'L':[0,-1], 'R':[0,1]}    
        directions = ['U','D','L','R']
        dp = {}
        dp[(0,0)] = master.isTarget()

        
        def dfs(i,j):

            for x in directions:
                if master.canMove(x) and (i + ijMap[x][0],j + ijMap[x][1]) not in dp:
                    master.move(x)
                    dp[(i + ijMap[x][0],j + ijMap[x][1])] = master.isTarget()
                    dfs(i + ijMap[x][0],j + ijMap[x][1])
                    
                    master.move(oppMap[x])
 
        dfs(0,0)
        
        q = deque([[0,0]])
        level = 0
        seen = set()
        while q:
            for i in range(len(q)):
            
                j,k = q.popleft()
                if dp[(j,k)] == True:
                    return level
                if (j,k) in seen:
                    continue
                seen.add((j,k))
                for x,y in ijMap.values():
                    
                    newx,newy = j + x, k + y
                    if (newx,newy) in seen or (newx,newy) not in dp:
                        continue
                    
                    q.append([newx,newy])
            level +=1
                    
        
        return -1
                    