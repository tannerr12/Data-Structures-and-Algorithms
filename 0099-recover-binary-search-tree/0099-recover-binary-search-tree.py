# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def dfs(root):
            nonlocal arr
            if root is None:
                return root

            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
            
            return root
        
        
        dfs(root)
        
        
        
        arr.sort(reverse=True)
        #print(arr)
        def build(root):
            nonlocal arr
            if root is None:
                return root
            
            build(root.left)
            
            root.val = arr.pop()
            
            build(root.right)
        
            return root
        
        
        return build(root)
            
        
                    