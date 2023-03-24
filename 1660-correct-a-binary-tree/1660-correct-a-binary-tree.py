# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        r = root
        
        q = deque()
        q.append((root, None, ''))
        seen = set()
        while q:
            
            for i in range(len(q)):
                
                node,par,direc = q.popleft()
                seen.add(node)
                if node.right:
                    if node.right in seen:
                        if direc == 'l':
                            par.left = None
                        else:
                            par.right = None
                        
                        break
                    
                    q.append((node.right, node, 'r'))
                
                if node.left:
                    q.append((node.left, node, 'l'))
                    
                
        return r
                