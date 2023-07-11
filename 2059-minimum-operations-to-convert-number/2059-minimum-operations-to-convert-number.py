class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:

        q = deque()
        q.append(start)
        level = 0
        seen = set()
        seen.add(start)
        while q:
            
            for i in range(len(q)):
                val = q.popleft()
                
            
                if val == goal:
                    return level
                
                for v in nums:
                    if val + v not in seen and ((val + v <= 1000 and val + v >= 0) or val + v == goal):
                        seen.add(val + v)            
                        q.append(val + v)
                    if val - v not in seen and ((val - v <= 1000 and val - v >= 0) or val - v == goal):
                        seen.add(val - v)
                        q.append(val - v)
                    if val ^ v not in seen and ((val ^ v <= 1000 and val ^ v >= 0) or val ^ v == goal):
                        seen.add(val ^ v)
                        q.append(val ^ v)
                        
            level += 1
        
        return -1