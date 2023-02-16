# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        highl = 1
        highr =1
        if root.left:
            highl = self.maxDepth(root.left) +1
        if root.right: 
            highr = self.maxDepth(root.right) +1
        
        return max(highl,highr) 