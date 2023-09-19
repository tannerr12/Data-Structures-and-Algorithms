# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
       
        
        def dfs(root):
            
            if root is None:
                return [True,0,False,0]
            
            Tmin = float('inf')
            Fmin = float('inf')
            left = dfs(root.left)
            right = dfs(root.right)
            
            if root.val == 0:
                return [True, 1, False, 0]
            elif root.val == 1:
                return [True, 0, False, 1]
            
            elif root.val == 2:

                #True and True
                Tmin = min(Tmin, left[1] + right[1])
                
                #False and True
                Tmin = min(Tmin, left[3] + right[1])
                
                #True and False
                Tmin = min(Tmin, left[1] + right[3])
                    
                #False + False
                Fmin = min(Fmin, left[3] + right[3])
                
                     
                    
            elif root.val == 3:
                #True + True
                Tmin = min(Tmin, left[1] + right[1])

                #True + False
                Fmin = min(Fmin, left[1] + right[3])
                
                #False + True
                Fmin = min(Fmin, left[3] + right[1])
                
                #False + False
                Fmin = min(Fmin, left[3] + right[3])

           
            elif root.val == 4:
                
                #False + True
                Tmin = min(Tmin, left[3] + right[1])

                #True + False
                Tmin = min(Tmin, left[1] + right[3])
                
                #False + False
                Fmin = min(Fmin, left[3] + right[3])
                
                Fmin = min(Fmin, left[1] + right[1]) 

            else:
                
                Tmin = min(Tmin, left[3] + right[3])
                Fmin = min(Fmin, left[1] + right[1])
            
            return [True,Tmin,False,Fmin]
        
        
        res = dfs(root)
        
        if result:
            return res[1]
        else:
            return res[3]
                