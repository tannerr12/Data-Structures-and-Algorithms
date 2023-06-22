# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        
        def find(node,tar):
            
            if node is None:
                return False
            if node.val == tar:
                return True
            
            res = False
            if tar > node.val:
                res = res or find(node.right, tar)
            
            if tar < node.val:
                res = res or find(node.left, tar)
            
            
            return res
        
        def dfs(root):
            
            if root is None:
                return False
            
            res = False
            res = res or dfs(root.left)
            
            res = res or find(root2, target - root.val)
            
            res = res or dfs(root.right)
            
            return res
        
        
        return dfs(root1)