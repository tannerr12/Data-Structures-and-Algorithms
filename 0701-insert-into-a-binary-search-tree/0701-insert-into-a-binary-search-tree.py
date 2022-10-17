# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        broot = root
        
        
        def dfs(root):
            
            if root is None:
                root = TreeNode(val)
                
            
            
            
            elif root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    dfs(root.left)
                
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    dfs(root.right)
                    
            
            
            
            return root
        
        
        return dfs(root)
                
            
            
            