# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        q = deque()
        
        q.append([root,1])
        
        level = 0
        
        res = 0
        while q:
            res = max(res, abs(q[0][1] - q[-1][1]))
            for i in range(len(q)):
                
                node,k = q.popleft()
                
                if node.left:
                    q.append([node.left,k*2 -1])
                if node.right:
                    q.append([node.right, k * 2])
            
            
         
        
        
        return res +1