class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        
        mxY,mnY,mxX,mnX = 0,float('inf'),0,float('inf')
        
        q = deque([[x,y]])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        seen = set()
        seen.add((x,y))
        while q:
        
            for i in range(len(q)):
                
                m,n = q.popleft()
                
                mxY = max(mxY, n)
                mnY = min(mnY, n)
                mxX = max(mxX, m)
                mnX = min(mnX, m)
                
                
                
                for a,b in directions:
                    newx = m + a
                    newy = n + b
                    
                    if newx < 0 or newy < 0 or newx >= len(image) or newy >= len(image[0]) or image[newx][newy] != "1" or (newx,newy) in seen:
                        continue
                    seen.add((newx,newy))
                    q.append([newx,newy])
                
        
    
        return (mxX - mnX + 1) * (mxY - mnY + 1)