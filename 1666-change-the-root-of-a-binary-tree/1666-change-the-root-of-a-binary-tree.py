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
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        #test leaf
        def dfs2(root):
            
            if not root:
                return None
            
            print('val ' + str(root.val))
            print('parent ' + str(root.parent.val))
            dfs2(root.left)
            dfs2(root.right)
        
        found = False
        def dfs(root,par):
            nonlocal found
            if not root:
                return None

            if root == leaf:
                found = True
            
            #print(root.val)
            if root.left and not found:
                dfs(root.left,root)
                
            if root.right and not found:
                dfs(root.right, root)
            
            if found and par is not None:
                if root.left:
                    root.right = root.left
                
                root.left = par
                if par and par.left == root:
                    par.left = None
                    par.parent = root
                elif par:
                    par.right = None
                    par.parent = root
                
                return root
            return root
            
            
        dfs(root, None)      
        #dfs2(leaf)
        leaf.parent = None
        return leaf
    
    

        
            
            