class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        dp = []
        for x,y in lights:
            
            start = x - y
            end = x + y + 1
            
            dp.append([start, 1])
            dp.append([end,-1])
        
        
        dp.sort()
        
        total = 0
        res =[0,0]
        for pos,val in dp:
            
            total += val
            if total > res[0]:
                res = [total,pos]
        
        
        return res[1]