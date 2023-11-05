# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node):
            
            if node is None:
                return [0, True, float('-inf'), float('inf')]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left[1] and right[1]:
                if (node.left is None or (node.left and left[2] < node.val)) and (node.right is None or (node.right and right[3] > node.val)):
                    return [left[0] + right[0] + 1, True, max(right[2], left[2],node.val), min(left[3], right[3], node.val)]
                
             
            return [max(left[0], right[0],),False,max(left[2], node.val, right[2]), min(right[3], node.val,left[3])]
        
        
        return dfs(root)[0]