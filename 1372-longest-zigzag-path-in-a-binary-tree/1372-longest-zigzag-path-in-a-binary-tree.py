# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        r = 0
        @cache
        def dfs(root,count,depth):
        
            
            if root is None:
                return depth -1
            res = 0
            if count % 2 == 0:
                res = max(res,dfs(root.left, count+1,depth+1))
                res = max(res,dfs(root.right,0,1))
            else:
                res = max(dfs(root.right,count+1,depth+1),res)
                res = max(res,dfs(root.left,1,1))
           
            

            return res
        #left
        r = max(r,dfs(root,0,0))
        #right
        r = max(r,dfs(root,1,0))

        return r

