# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> int:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        
        directions = ['U', 'D', 'L', 'R']
        mp = {'U': [-1,0], 'D': [1, 0], 'L': [0,-1], 'R':[0,1]}
        opposite = {'U':'D', 'D':'U', 'L':'R', 'R':'L'}
        seen = defaultdict(int)
        seen[(0,0)] = 0
        i,j = 0,0
        ans = float('inf')
        target = (0,0)
        def dfs(i,j):
            nonlocal target
            if master.isTarget():
                target = (i,j)
                return True
            
            res = False
            
            #try all 4 directions
            for x in directions:
                newx,newj = i + mp[x][0], j + mp[x][1]
                if (newx,newj) in seen:
                    continue
                seen[(newx,newj)] = float('inf')
                if master.canMove(x):
                    val = master.move(x)
                    seen[(newx,newj)] = val
                    res = res | dfs(newx,newj)
                    #move back to reverse the move operation
                    master.move(opposite[x])
            
            
            
            return res
        
        val = dfs(i,j)
        
        if not val:
            return -1
        
        
        heap = [[0,0,0]]
        s = set()
        s.add((0,0))
        while heap:
            
            c,x,y = heappop(heap)
            
            if (x,y) == target:
                return c
            
            for a,b in mp.values():
                
                nx,ny = x + a, y + b
                if seen[(nx,ny)] == float('inf') or (nx,ny) in s:
                    continue
                
                s.add((nx,ny))
                heappush(heap,(c + seen[(nx,ny)], nx, ny))
                
                
            
            
        
    