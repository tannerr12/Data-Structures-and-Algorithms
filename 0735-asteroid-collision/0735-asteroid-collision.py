class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        
        
        stack = []
        negsur = []
        for i in range(len(a)):
            
            #anything that is positive just add to stack
            if a[i] >= 0:
                stack.append(a[i])
            
            else:
                #if our negative astroid is larger keep crushing our stack
                while stack and abs(a[i]) > stack[-1]:
                    stack.pop()
                
                #it crushed the whole stack, it survives
                if not stack:
                    negsur.append(a[i])
                
                #it hit an astroid of the same size they both die
                elif stack and stack[-1] == abs(a[i]):
                    stack.pop()
        
        
        #negatives always have to be at the beginning & positives at the end
        return negsur + stack