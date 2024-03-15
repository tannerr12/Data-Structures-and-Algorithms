class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        f = set(forbidden)
        '''
        @cache
        def dfs(pos):
            
            if pos == x:
                return 0
            elif pos > (x * 3):
                return float('inf')
            
            res = float('inf')
            
            #jump forward
            if pos + a not in f:
                res = min(res, dfs(pos + a) + 1)
            #jump back than forward
            if pos - b >= 0 and pos-a not in f and pos-b+a not in f:
                res = min(res, dfs(pos - b + a) + 2)
            #jump only back (we are b moves from x)
            if pos - b == x:
                return 1
            
            
            return res
            
        '''
        furthest = max(x, max(forbidden)) + a + b
        q = deque([[0,0]])
        level = 0
        seen = set()
        seen.add((0,0))
 

        
   
        while q:
            
            for i in range(len(q)):
                pos,d = q.popleft()
                
                if pos == x:
                    return level
                
                #jump forward
                if pos + a <= furthest and pos + a not in f and (pos + a, 0) not in seen:
                    seen.add((pos + a, 0))
                    q.append([pos + a, 0])
                #jump back than forward
                if not d and pos - b >= 0 and pos - b not in f and (pos - b, 1) not in seen and (pos - b, 0) not in seen:
                    seen.add((pos - b, 1))
                    q.append([pos - b, 1]) 

            level += 1
            
        return -1