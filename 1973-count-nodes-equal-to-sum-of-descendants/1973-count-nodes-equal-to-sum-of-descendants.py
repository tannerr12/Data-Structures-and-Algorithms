# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        
    

        def dfs(root):
            
            if root is None:
                return [0,0]
            
            
            cur1, r1 = dfs(root.left)
            cur2, r2 = dfs(root.right)
            
            
            if cur1 + cur2 == root.val:
                r1 +=1
            
            return [cur1 + cur2 + root.val,r1 + r2]
        
        
        return dfs(root)[1]
    
            