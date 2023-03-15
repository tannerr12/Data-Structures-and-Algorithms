# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        
        if root is None:
            return None
        
        r2 = NodeCopy(root.val, None, None, None)
        
        
        stack = []
        stack.append(root)
        stack.append(r2)
        mp = {}
        count = 0
        while stack:
            
            node2 = stack.pop()
            node = stack.pop()
            mp[node] = node2
            count +=1
            if node.left:
                stack.append(node.left)
                node2.left = NodeCopy(node.left.val, None, None, None)
                stack.append(node2.left)
            
            if node.right:
                stack.append(node.right)
                node2.right = NodeCopy(node.right.val, None, None, None)
                stack.append(node2.right)
        
        
        
      
        stack = []
        stack.append(root)
        stack.append(r2)
        while stack:
            
            node2 = stack.pop()
            node = stack.pop()
            
            if node.random in mp:
                n = mp[node.random]
                node2.random = n
                
            if node.left:
                stack.append(node.left)
                stack.append(node2.left)
            
            if node.right:
                stack.append(node.right)
                stack.append(node2.right)
        
        return r2
     
        
            
        
        