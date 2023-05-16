# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, node: Optional[TreeNode], voy: List[int]) -> List[int]:
        
        i = 0
        score = []
        p = False
        def dfs(root):
            nonlocal i,score,p   
            if i >= len(voy)-1 and root.val == voy[i]:
                p = True
                return score
            elif i >= len(voy)-1:
                return [-1]

            
            if root.val != voy[i]:
                return [-1]
            
            #try flip
            if i < len(voy) and root.left and root.left.val != voy[i+1]:
                root.left,root.right = root.right,root.left
                
                score.append(root.val)
                if root.left and root.left.val == voy[i+1]:
                    i += 1
                    dfs(root.left)
                if root.right and root.right.val == voy[i+1]:
                    i +=1
                    dfs(root.right)
                root.left,root.right = root.right,root.left
     
            else:
                #dont flip
                if root.left and root.left.val == voy[i+1]:
                    i+=1
                    dfs(root.left)
                if root.right and root.right.val == voy[i+1]:
                    i+=1
                    dfs(root.right)
            
            
     
        
        
        dfs(node)
        return score if p else [-1]
            