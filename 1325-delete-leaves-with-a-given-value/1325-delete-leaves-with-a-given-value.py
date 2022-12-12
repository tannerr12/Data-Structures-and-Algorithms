# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(root):
            
            if root is None:
                return False

            if dfs(root.left):
                root.left = None
            if dfs(root.right):
                root.right = None

            if root.right is None and root.left is None and root.val == target:
                return True
        
        
        dfs(root)
        
        return root if root.left != None or root.right != None or root.val != target else None
            