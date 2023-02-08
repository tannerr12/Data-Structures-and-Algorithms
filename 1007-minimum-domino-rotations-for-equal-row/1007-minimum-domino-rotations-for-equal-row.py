class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        targets = [tops[0]]
        if tops[0] != bottoms[0]:
            targets.append(bottoms[0])
        
        res = float('inf')
        for i in range(len(targets)):
            goal = targets[i]
            top,bottom = 0,0
            skip = False
            for x,y in zip(tops, bottoms):
                
                if x != goal and y != goal:
                    skip = True
                    break
                    
                if x == goal and y != goal:
                    bottom +=1
                
                elif y == goal and x != goal:
                    top +=1
                
            if not skip:
                res = min(res, top, bottom)
        
        return res if res != float('inf') else -1