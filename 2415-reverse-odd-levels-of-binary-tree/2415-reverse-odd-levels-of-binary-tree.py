# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        """
        def dfs(root,depth):
            
            if root is None:
                return root
            
            if depth % 2 == 0 and root.left:
                l = root.left.val
                root.left.val = root.right.val
                root.right.val = l
            
            dfs(root.left, depth +1)
            dfs(root.right, depth +1)
            
            return root
        
        
        return dfs(root,0)
    
           """
        
        q = deque()
        
        q.append(root)
        level = 0
        while q:
     
            if level % 2:
                
                r = []
                for i in range(len(q) -1,-1,-1):
                    r.append(q[i].val)
                    
            
            
            for i in range(len(q)):
                
                node = q.popleft()
                if level % 2:
                    
                    node.val, r[i] = r[i],node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
             
                
            level +=1
        
        return root
            