class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        mp = defaultdict(int)
        
        mx = 0
        start = defaultdict(int)
        arr = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] != 0 and forest[i][j] != 1:
                    mx = max(mx, forest[i][j])
                    start[forest[i][j]] = (i,j)
                    arr.append(forest[i][j])
        
        start[0] = (0,0)
        arr.append(0)
        arr.sort()
        def hadlocks(forest, sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            processed = set()
            deque = collections.deque([(0, sr, sc)])
            while deque:
                detours, r, c = deque.popleft()
                if (r, c) not in processed:
                    processed.add((r, c))
                    if r == tr and c == tc:
                        return abs(sr-tr) + abs(sc-tc) + 2*detours
                    for nr, nc, closer in ((r-1, c, r > tr), (r+1, c, r < tr),
                                           (r, c-1, c > tc), (r, c+1, c < tc)):
                        if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                            if closer:
                                deque.appendleft((detours, nr, nc))
                            else:
                                deque.append((detours+1, nr, nc))
            return -1
            
        

        res = 0
        
        for i in range(len(arr)-1):
            x,y = start[arr[i]]
            x2,y2 = start[arr[i+1]]
            val = hadlocks(forest, x,y,x2,y2)
            if val == -1:
                return -1
            else:
                res += val
        return res
            
                
                
            