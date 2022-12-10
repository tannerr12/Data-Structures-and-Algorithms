# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        h = []
        mx = float('-inf')
        mn = float('inf')
        def dfs(root):
 
            if root is None:
                return 0
            
            h.append(root.val)
        
            val = max(root.val,dfs(root.left),dfs(root.right))
            return val
        
        
        
        mx = max(mx, dfs(root1), dfs(root2))

        
        res = sorted(h,key=lambda x:x)
        return res
        