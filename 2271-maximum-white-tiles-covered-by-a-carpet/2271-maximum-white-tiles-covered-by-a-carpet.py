class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        
        
        prefix = [[float('inf'),float('inf'),0]]
        mx = 0
        for i in range(len(tiles)-1,-1,-1):
            x,y = tiles[i]
            
            prefix.append([x,y,prefix[-1][2] + y - x + 1])
            mx = max(mx, y)
            
        prefix.reverse()
        res = 0
        for i in range(len(tiles)-1,-1,-1):
            
            x,y = tiles[i]
            idx = bisect_left(prefix, x + carpetLen, key=lambda x:x[0])
            if x + carpetLen < prefix[idx][0]:
                idx -= 1
            cur = prefix[i][2] - prefix[idx][2] + (min(x + carpetLen,prefix[idx][1] + 1) - prefix[idx][0])
            res = max(res, cur)
            #print(prefix[idx])
            
        return res