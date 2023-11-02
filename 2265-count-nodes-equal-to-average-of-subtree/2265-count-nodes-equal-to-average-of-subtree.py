# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def dfs(root):
            nonlocal res
            if root is None:
                return [0,0]
            
            
            rnodes, rtotal = dfs(root.right)
            lnodes, ltotal = dfs(root.left)
            
            if ((rtotal + ltotal + root.val) // (rnodes + lnodes + 1)) == root.val:
                res +=1
            
            return [lnodes + rnodes + 1, rtotal + ltotal + root.val]
        
        dfs(root)
        return res
            