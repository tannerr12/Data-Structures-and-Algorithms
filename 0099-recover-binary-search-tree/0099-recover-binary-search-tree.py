# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x,y,pred = None,None,None
        def dfs(root):
            nonlocal x,y,pred
            if root is None:
                return root

            dfs(root.left)
            if pred and pred.val > root.val:
                
                y = root
                if x is None:
                    x = pred
                
                else:
                    return
                
            pred = root
            dfs(root.right)
            
            return root
        
        
        dfs(root)
        
        x.val, y.val = y.val, x.val
        
    
        
        
        
                    