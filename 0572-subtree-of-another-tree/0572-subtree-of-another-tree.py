# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.found = False
            
        def checkRoots(root,root2):
            if root is None:
                return 
            if root.val == root2.val:
                s = searchTree(root,root2)
                if s == True:
                    self.found = s
                
            
            checkRoots(root.left,root2)
            checkRoots(root.right,root2)
            
            
        def searchTree(root,root2):
            
            if root is None and root2 is None:
                return True
            elif root is None:
                return False
            elif root2 is None:
                return False
            
            
            if root.val == root2.val:
                b = ((searchTree(root.left,root2.left) and searchTree(root.right,root2.right)))
                
                return b
            
            else:
                     return False
                
        
        
        
        checkRoots(root,subRoot)
        return self.found