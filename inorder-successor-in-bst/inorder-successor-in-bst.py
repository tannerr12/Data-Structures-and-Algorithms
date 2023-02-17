# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        node = None
        def dfs(root):
            nonlocal node
            if root is None:
                return None
            
            if root.val > p.val:
                node = root
                dfs(root.left)
            else:
                dfs(root.right)
                
        
        dfs(root)
        
        
        
        
        return node