"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, r: 'Node', leaf: 'Node') -> 'Node':
        #test leaf
        def dfs2(root):
            
            if not root:
                return None
            
            print('val ' + str(root.val))
            if root.parent:
                print('parent ' + str(root.parent.val))
            dfs2(root.left)
            dfs2(root.right)
        
        
        def dfs(root,par):
    
            if not root:
                return None

            if root == r:
                root.parent = par
                return 
 
            if root.left:
                root.right = root.left

            root.left = root.parent
            if root.parent.left == root:
                root.parent.left = None
                
            else:
                root.parent.right = None
            
            p = root.parent
            root.parent = par
            
            dfs(p,root)
            return root
            
            
        dfs(leaf,None)      
        #dfs2(leaf)
        #leaf.parent = None
        return leaf
    
    

        
            
            