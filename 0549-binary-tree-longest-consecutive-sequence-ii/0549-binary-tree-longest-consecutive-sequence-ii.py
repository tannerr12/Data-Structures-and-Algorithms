# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            
            if not node:
                return [0,0,0]
            ans = [1,1,1]
            left = dfs(node.left)
            right = dfs(node.right)
            
            #left node is greater
            if node.left and node.left.val > node.val and node.left.val - node.val == 1:
                ans[1] = max(left[1] + 1, ans[1])
            #right node is greater
            if node.right and node.right.val > node.val and node.right.val - node.val == 1:
                ans[1] = max(right[1] + 1, ans[1])
            if node.right and node.right.val < node.val and node.right.val - node.val == -1:
                ans[0] = max(right[0] + 1, ans[0])
            if node.left and node.left.val < node.val and node.left.val - node.val == -1:
                ans[0] = max(left[0] + 1, ans[0])
            
            
            ans[2] = max(ans[2], ans[0] + ans[1] - 1,left[2], right[2])
            
            return ans
        
        
        res = dfs(root)
        
        return res[2]
            
            
            