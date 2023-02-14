"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        return self.encodeRecursive(root,[]) if root else None
    
    def encodeRecursive(self,root: 'Node', siblings):
        newNode = TreeNode(root.val)
        
        if siblings:
            newNode.left = self.encodeRecursive(siblings[0],siblings[1:])
        
        if root.children:
            newNode.right = self.encodeRecursive(root.children[0],root.children[1:])
        
        return newNode
    
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        return self.decodeRecursive(data,None) if data else None
    
    def decodeRecursive(self,root,parent):
        newNode = Node(val=root.val, children=[])
        if root.left:
            parent.children = [(self.decodeRecursive(root.left, parent))] + parent.children
        
        if root.right:
            newNode.children = [(self.decodeRecursive(root.right,newNode))] + newNode.children
        
        return newNode
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))