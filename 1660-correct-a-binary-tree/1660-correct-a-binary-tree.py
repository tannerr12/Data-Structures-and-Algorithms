# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        #We will do BFS right -> left and keep track of the parent
        q = deque()
        q.append((root, None))
        seen = set()
        while q:
            
            for i in range(len(q)):
                
                node,par = q.popleft()
                seen.add(node)
                if node.right:
                    if node.right in seen:
                        if par.left == node:
                            par.left = None
                        else:
                            par.right = None
                        
                        break
                    
                    q.append((node.right, node))
                
                if node.left:
                    q.append((node.left, node))
                    
                
        return root
                