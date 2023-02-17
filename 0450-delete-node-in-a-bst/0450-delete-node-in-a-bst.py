# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        def delNode(root,key):
            
            if root is None:
                return None
            
            if root.val > key:
                
                root.left = delNode(root.left, key)
            
            elif root.val < key:
                root.right = delNode(root.right, key)
                
            
            else:
                
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                
                
                #scan right side of leftmost
                
                cur = root.right
                
                while cur.left:
                    
                    cur = cur.left
                
                root.val = cur.val
                root.right = delNode(root.right,root.val)
                
            return root
        
        return delNode(root,key)