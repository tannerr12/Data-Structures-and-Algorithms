# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        def dfs(root):
            nonlocal total
            if root is None:
                return False,True
            
            c1,m1 = dfs(root.left)
            c2,m2 = dfs(root.right)
            
            camera, monitor = False, False
            
            if c1 or c2:
                monitor = True
            if not m1 or not m2:
                camera = True
                total +=1
                monitor = True
            
            
            return camera,monitor
        
        c,m = dfs(root)
        
        if not m:
            return total +1
        return total
            