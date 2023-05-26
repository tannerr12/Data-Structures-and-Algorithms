class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        stack = []
        mx = 0
        for i in range(len(preorder)):
            
            while stack and stack[-1] < preorder[i]:
                mx = max(mx,stack.pop())
            
            if preorder[i] < mx:
                return False
            
            stack.append(preorder[i])
        
        return True
            
            