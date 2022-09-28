class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        check = False
        starCount = 0
        barMap = {}
        prev = 0
        res = []
        memox = {}
        memoy = {}
        
        for i in range(len(s)-1,-1,-1):
            
            if check ==False and s[i] == '*':
                continue
            if check== False and s[i] == '|':
                check = True
            
            
            if s[i] == '*':
                starCount+=1
            
            elif s[i] == '|':
                if prev == 0:
                    barMap[i] = starCount
                    prev = i
                else:
                    barMap[i] = starCount
                    prev = i
            
        #print(barMap)
        
        for x,y in queries:
            countx = []
            county = []
            cx = x
            cy = y
            
            
            
            
            if cx not in memox:
                countx.append(cx)
                while cx < y-1 and cx not in barMap:
                    cx +=1
                    countx.append(cx)
            else:
                cx = memox[cx]
            if cy not in memoy:
                county.append(cy)
                while cy > x+1 and cy not in barMap:
                    cy -=1
                    county.append(cy)
            else:
                cy = memoy[cy]

            
            if cx in barMap and cy in barMap:
                if barMap[cx] - barMap[cy] < 0:
                    res.append(0)
                    continue
                res.append(barMap[cx] - barMap[cy])
                for val in countx:
                    memox[val] = cx
                for val in county:
                    memoy[val] = cy
            else:
                res.append(0)
         
        
        
        return res
            
            