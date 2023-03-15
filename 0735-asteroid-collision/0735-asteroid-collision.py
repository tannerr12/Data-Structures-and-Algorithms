class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        
        
        stack = []
        negsur = []
        for i in range(len(a)):
            
            if a[i] >= 0:
                stack.append(a[i])
            
            else:
                
                while stack and abs(a[i]) > stack[-1]:
                    stack.pop()
                
                if not stack:
                    negsur.append(a[i])
                elif stack and stack[-1] == abs(a[i]):
                    stack.pop()
        
        
        return negsur + stack