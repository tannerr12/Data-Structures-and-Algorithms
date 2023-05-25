class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        
        stack = []
        res = [float('inf')] * len(cars)
        newSpeed = [0] * len(cars)
        for i in range(len(cars)-1,-1,-1):
            x,y = cars[i]
            while stack and stack[-1][1] >= y:
                a,b,c = stack.pop()
            
            if stack:
                while len(stack) >= 2 and abs((stack[-1][0] - x)) / abs((stack[-1][1] - y)) >= abs((stack[-2][0] - x)) / abs((stack[-2][1] - y)):
                    stack.pop()
                
                res[i] = min(res[i], abs((stack[-1][0] - x)) / abs((stack[-1][1] - y)))
                
            else:
                res[i] = -1
                
            
        
            stack.append((x,y,i))
        

            
        return res