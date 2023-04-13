class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        stack = []
        
        pushed = deque(pushed)
        popped = deque(popped)
        seen = set()
        while popped:
            
            if popped[0] not in seen:
                val = None
                while pushed and val != popped[0]:
                    val = pushed.popleft()
                    stack.append(val)
                    seen.add(val)
            
            
            if not stack or stack[-1] != popped[0]:
                return False
            
            stack.pop()
            popped.popleft()
        
        return True
            
            