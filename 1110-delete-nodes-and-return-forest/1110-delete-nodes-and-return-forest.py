# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        d = set(to_delete)
        
        
        q = deque()
        
        q.append((root,None))
        
        res = []
        while q:
            
            for i in range(len(q)):
                 
                node, par = q.popleft()
                
                if par == None and node.val not in d:
                    res.append(node)
                    
                bad = False
                if node.val in d:
                    bad = True
                
                if bad and par:
                    if par.right == node:
                        par.right = None
                    else:
                        par.left = None
                
                if node.left:
                    
                    if bad:
                        q.append((node.left, None))
                    else:
                        q.append((node.left, node))
                        
                if node.right:
                    if bad:
                        q.append((node.right, None))
                    else:
                        q.append((node.right, node))
                
                
                if bad and not par:
                    node.left = None
                    node.right = None
        
        return res