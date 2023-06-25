# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        
        
        def getSum(root):
            
            if root is None:
                return 0
            
            
            
            l = getSum(root.left)
            
            r = getSum(root.right)
            
            return l + r + root.val
        
        total = getSum(root)
        
        #print(total)
        if total % 2:
            return False
        res = False
        def dfs(node):
            nonlocal res,total,root
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            if l + r + node.val == total - (l + r + node.val) and node != root:
                res = True
            
            return l + r + node.val
        
        
        dfs(root)
        
        return res