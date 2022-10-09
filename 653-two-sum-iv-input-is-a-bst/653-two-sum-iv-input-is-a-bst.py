# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        hmap = set()
        if not root:
            return False
        q = deque()
        q.append(root)
        
        
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                
                target = k - node.val
                if target in hmap:
                    return True
                hmap.add(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False
            
                
        