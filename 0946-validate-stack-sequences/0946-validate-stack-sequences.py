class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        stack = []
        
        l,r = 0,0
        seen = set()
        while r < len(popped):
            
            if popped[r] not in seen:
                val = None
                while l < len(pushed) and val != popped[r]:
                    val = pushed[l]
                    stack.append(val)
                    seen.add(val)
                    l +=1
            
            
            if not stack or stack[-1] != popped[r]:
                return False
            
            stack.pop()
            r +=1
        
        return True
            
            