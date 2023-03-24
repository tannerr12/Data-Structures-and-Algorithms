# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        res = 0
        def dfs(root):
            nonlocal res
            
            if root.left is None and root.right is None:
                res +=1
                return [True, root.val]
            
            stat,statr = True,True
            val,valr = root.val,root.val
            if root.left:
                stat,val = dfs(root.left)
            if root.right:
                statr,valr = dfs(root.right)
            
            if stat and statr and val == valr == root.val:
                res +=1
                return [True,root.val]
            else:
                return [False,root.val]
        
        dfs(root)
        return res