# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.ll = TreeNode()
        self.hold = self.ll
        
        def dfs(root):
            
            if root is None:
                return
            
                
            self.ll.right = TreeNode()
            self.ll = self.ll.right
            self.ll.val = root.val
            self.ll.left = None
            
            
            dfs(root.left)
            dfs(root.right)
            
     
        def assign(root):
            
            if root is None:
                return
            self.hold = self.hold.right
            print(self.hold)
            root.left = None
            root.val = self.hold.val
            root.right = self.hold.right
            root = root.right
           
         
            
        dfs(root)
        assign(root)
     
       # root = self.hold.right
       
        #$print(hold)
        
        