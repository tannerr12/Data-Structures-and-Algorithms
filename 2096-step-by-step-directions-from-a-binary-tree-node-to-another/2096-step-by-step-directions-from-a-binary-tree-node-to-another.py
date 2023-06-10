# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    
        p1 = []
        p2 = []
        path = []
        def dfs(node):
            nonlocal p1,path
            if node is None:
                return
            if node.val == destValue:
                p1 = path.copy()
                return
            
            path.append('L')
            dfs(node.left)
            path.pop()
            path.append('R')
            dfs(node.right)
            path.pop()
            
        def dfs2(node):
            nonlocal p2,path
            if node is None:
                return
            if node.val == startValue:
                p2 = path.copy()
                return
            
            path.append('L')
            dfs2(node.left)
            path.pop()
            path.append('R')
            dfs2(node.right) 
            path.pop()
            
        dfs(root)
        dfs2(root)
        
        
        #print(p1)
        #print(p2)
        start = 0
        i = 0 
        
        while i < max(len(p1), len(p2)):
            if i >= min(len(p1), len(p2)):
                start = i
                break
            
            if p1[i] != p2[i]:
                start = i
                break
            i+=1
                
        ans = []
        for i in range(start, len(p2)):
            ans.append('U')
        
        for i in range(start, len(p1)):
            ans.append(p1[i])
        
        
        return ''.join(ans)