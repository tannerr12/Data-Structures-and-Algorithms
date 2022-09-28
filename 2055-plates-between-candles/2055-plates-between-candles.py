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
            memox[i] = prev
            if check ==False and s[i] == '*':
                continue
            if check== False and s[i] == '|':
                check = True
            
            
            if s[i] == '*':
                starCount+=1
            
            elif s[i] == '|':

                barMap[i] = starCount
                prev = i
            memox[i] = prev
        for i in range(len(s)):

            if s[i] == '|':
                prev = i
            memoy[i] = prev

        for x,y in queries:
            cx = memox[x]
            cy = memoy[y]
            
            if cy >= x and cx <= y and cx in barMap and cy in barMap:
               # if barMap[cx] - barMap[cy] < 0:
                #    res.append(0)
                #    continue
                res.append(barMap[cx] - barMap[cy])
             
            else:
                res.append(0)
         
        
        
        return res
            
            