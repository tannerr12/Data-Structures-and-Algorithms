class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        
        l,r = 0,0
        
        
        res = []
        while True:
            if l >= len(firstList) or r >= len(secondList):
                break
        
            a,b = firstList[l]
            
            x,y = secondList[r]
            m,n = max(x,a), min(b,y)
            
            if m <= n:
                res.append([max(x,a),min(b,y)])
                        
            if b > y:
                r +=1
            elif y > b:
                l +=1
            
            else:         
                l +=1
                r +=1


        
        
        return res