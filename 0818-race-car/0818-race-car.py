class Solution:
    def racecar(self, target: int) -> int:
        
        
        level = 0
        q = deque([[0,1]])
        seen = set()
        seen.add((0,1))
        while q:
            
            for i in range(len(q)):
                
                pos,speed = q.popleft()
                flipSpeed = -1 if speed > 0 else 1
                
                if pos == target:
                    return level
                
                if pos + speed <= target * 2 and (pos + speed, speed * 2) not in seen:
                    seen.add((pos + speed, speed * 2))
                    q.append((pos + speed, speed * 2))
                if (pos, flipSpeed) not in seen:
                    seen.add((pos,flipSpeed))
                    q.append((pos, flipSpeed))
            
            
            level += 1
        
        
 
            
            
        
        
        
        
                
                
                
                