# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            parent = TreeNode(val)
            parent.left = root
            return parent
        
        q = deque([root])
        d = 1
        while q:
            
            for i in range(len(q)):
            
                node = q.popleft()
                
                #add a layer of nodes
                if d == depth -1:
                    left = node.left
                    right = node.right
                    
                    l = TreeNode(val)
                    r = TreeNode(val)
                    node.left = l
                    node.right = r
                    l.left = left
                    r.right = right
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
                
                    
            d += 1
        
        return root