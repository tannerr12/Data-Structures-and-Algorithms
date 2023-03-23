# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pointer = None
        def dfs(root,par):
            nonlocal pointer
            if root is None:
                return None
            if root.left is None and root.right is None:
                pointer = root
            
            dfs(root.left, root)
            
            #once we hit a leaf node we want to flip the parents left and right to None to avoid a cycle
            #we will need the parents right so lets save that, We than assign this nodes right = parent node and the 
            #left to be equal to the parents right. Since rights only go 1 level deep we dont need to traverse the right side of the
            #tree at all and just need to get to the bottom of the left than go from there. Another thing to note is by the time we get back to the top
            #our root is now a leaf so if we reach a leaf node we should save that so it can be returned later
            if par:
                right = par.right
                par.left = None
                par.right = None
                root.right = par
                root.left = right
            
            
            return root
        
        dfs(root, None)
        return pointer
            