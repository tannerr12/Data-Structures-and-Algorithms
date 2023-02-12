class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        q = deque()
        
        q.append(0)
        
        seen = set()
        seen.add(0)
        
        while q:
            
            for i in range(len(q)):
                
                node = q.popleft()
                
                for key in rooms[node]:
                    
                    if key not in seen:
                        q.append(key)
                        seen.add(key)
        
        return len(seen) == len(rooms)