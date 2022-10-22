class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        memo = {}
        
        def dfs(r,c):
            
            if (r,c) in memo:
                return memo[(r,c)]
            if r == destination[0] and c == destination[1]:
                return True
            
            memo[(r,c)] = False
            b = False
            tempr = r
            while tempr >= 0 and maze[tempr][c] != 1:
                tempr -=1
            
            
            if tempr +1 != r:
                #up
                b = b or dfs(tempr+1,c)
                
            tempr = r
            while tempr < len(maze) and maze[tempr][c] != 1:
                tempr +=1
            
            if tempr -1 != r:
                #down
                b = b or dfs(tempr-1,c)
            
            
            
            tempc = c
                    
                
            while tempc < len(maze[0]) and maze[r][tempc] != 1:
            
                tempc +=1
            
            if tempc -1 != c:
                #right
                b = b or dfs(r,tempc -1)
                
            tempc = c
            while tempc >= 0 and maze[r][tempc] != 1:
                tempc -=1
            
            if tempc +1 != c:
                #left
                b = b or dfs(r,tempc +1)
            
            
           
            return b
            
            
            
        return dfs(start[0], start[1])
        
        
            
            