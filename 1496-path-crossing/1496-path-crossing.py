class Solution:
    def isPathCrossing(self, path: str) -> bool:
        v,h = 0,0
        seen = set()
        seen.add((0,0))
        for i in range(len(path)):
            
            if path[i] == 'N':
                v += 1
            elif path[i] == 'S':
                v -= 1
            elif path[i] == 'E':
                h += 1
            else:
                h -= 1
            if (v,h) in seen:
                return True
            seen.add((v,h))
            
        
        return False