# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        
        
        
        q = deque()
        
        q.append(root)
        
        while q:
            found = False
            for i in range(len(q)):
                
                node= q.popleft()
                    
                if not found:
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                else:
                    return node
                
                if node == u:
                    found = True
        
        
        
        return None