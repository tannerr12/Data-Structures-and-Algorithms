class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        c = Counter(tops + bottoms)
        targets = []
        
        for key,val in c.items():
            
            if val >= len(tops):
                targets.append(key)
        
        res = float('inf')
        for i in range(len(targets)):
            goal = targets[i]
            top = 0
            bottom = 0
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