class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        
        q = deque([x])
        dist = 0
        seen = set()
        seen.add(x)
        
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node == y:
                    return dist
                
                if node % 11 == 0 and node // 11 not in seen:
                    seen.add(node // 11)
                    q.append(node // 11)
                if node % 5 == 0 and node // 5 not in seen:
                    seen.add(node // 5)
                    q.append(node // 5)
                
                if node - 1 not in seen:
                    seen.add(node - 1)
                    q.append(node - 1)
                
                if node + 1 not in seen:
                    seen.add(node + 1)
                    q.append(node + 1)
            
            dist += 1
        
        return -1
                    
                    