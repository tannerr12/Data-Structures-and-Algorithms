# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        rootval = [root.val]
        left = []
        right = []
        leaf = []
        
        if root.left is None and root.right is None:
            return rootval
        
        def dfsFindBound(root,t):
            
            if root is None:
                return 
    
            if t == 'left' and (root.left or root.right):
                left.append(root.val)
            elif t == 'right' and (root.left or root.right):
                right.append(root.val)
                
            if t == 'left':
                if root.left:
                    dfsFindBound(root.left,t)
                else:
                    dfsFindBound(root.right,t)
            else:
                if root.right:
                    dfsFindBound(root.right,t)
                else:
                    dfsFindBound(root.left,t)
        
        def dfsFindLeaf(root):
            
            if root is None:
                return
            
            if root.left is None and root.right is None:
                leaf.append(root.val)
            
            
            dfsFindLeaf(root.left)
            dfsFindLeaf(root.right)
        
        dfsFindBound(root.left,'left')
        dfsFindBound(root.right,'right')
        dfsFindLeaf(root)
        
        #print(rootval)
        #print(left)
        #print(right)
        #print(leaf)
        right = right[::-1]
        
        return rootval + left + leaf + right
                
            