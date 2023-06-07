class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        
        player = abs(0 - target[0]) + abs(0 - target[1])
        
        for x,y in ghosts:
            
            mandist = abs(x - target[0]) + abs(y - target[1])
            if mandist <= player:
                return False
        
        return True