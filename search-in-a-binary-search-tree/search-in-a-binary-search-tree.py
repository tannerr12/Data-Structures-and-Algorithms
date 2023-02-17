# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        
        def dfs(root):
            
            if root is None:
                return None
            
            
            if root.val == val:
                return root
            
            b= None
            if val > root.val:
                b = b or dfs(root.right)
                
            else:
                b = b or dfs(root.left)
                
            
            return b
          
        
        
        return dfs(root)