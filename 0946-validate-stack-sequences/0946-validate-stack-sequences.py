class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        
        stack = []
        
        l,r = 0,0
        
        while r < len(popped):
            
            if not stack or popped[r] != stack[-1]:
                val = None
                while l < len(pushed) and val != popped[r]:
                    val = pushed[l]
                    stack.append(val)
                    l +=1
            
            
            if not stack or stack[-1] != popped[r]:
                return False
            
            stack.pop()
            r +=1
        
        return True
            
            