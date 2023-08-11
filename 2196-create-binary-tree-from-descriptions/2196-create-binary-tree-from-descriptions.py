# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        
        mp = {}
        cand = set()
        for x,y,z in descriptions:
            cand.add(x)
            cand.add(y)
            
        for x,y,z in descriptions:
            p,t = None, None
            cand.remove(y)
            if x not in mp:
                p = TreeNode(x)
                mp[x] = p
            else:
                p = mp[x]
            if y not in mp:
                t = TreeNode(y)
                mp[y] = t
            else:
                t = mp[y]
                
            if z == 1:
                p.left = t
            else:
                p.right = t
        
        
        par = list(cand)[0]
        return mp[par]
        
        
            
            