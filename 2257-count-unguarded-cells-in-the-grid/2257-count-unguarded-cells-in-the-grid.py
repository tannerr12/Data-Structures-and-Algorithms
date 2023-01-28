class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        
        
        gMap = defaultdict(list)
        
        grid = [[0 for j in range(n)] for i in range(m)]
        
        
        """
        def binarySearch(target, check):
            
            l,r = 0, len(check) -1
            
            while l < r:
                
                mid = (l+r) //2
                
                if check[mid] > target and check[mid]
        """
        
        for x,y in guards:
            
            grid[x][y] = 'G'

        
        for x,y in walls:
            
            grid[x][y] = 'W'

        
        #print(grid)
        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0:
                    val = grid[r][c]
                    gMap['r' + str(r)].append((c,val))
                    gMap['c' + str(c)].append((r, val))
        
        #print(gMap)
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    #scan for closest between row/col up/down left/right if all W or out of bounds its good
                    #if any are guard its not good
                    arrC = gMap['r' + str(r)]
                    arrR = gMap['c' + str(c)]
                   
                    cIdx = 0
                    rIdx = 0
                    if len(arrC) > 0:
                        cIdx = bisect.bisect_left(arrC, c,key=lambda i: i[0])
                        cIdx -=1
                        if cIdx >= 0 and arrC[cIdx][1] == 'G':
                            continue
                        if cIdx + 1 < len(arrC) and arrC[cIdx+1][1] == 'G':
                            continue
                    if len(arrR) > 0:
                        rIdx = bisect.bisect_left(arrR, r,key=lambda i: i[0])
                        rIdx -=1

                        if rIdx >= 0 and arrR[rIdx][1] == 'G':
                            continue
                        if rIdx + 1 < len(arrR) and arrR[rIdx+1][1] == 'G':
                            continue
                    res +=1
                    #print(cIdx)
                    #print(rIdx)
        
        
        return res
                
        