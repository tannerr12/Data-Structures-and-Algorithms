class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
       
        
        def dfs(root):
            
            if root is None:
                return [0,0]
            
            Tmin = float('inf')
            Fmin = float('inf')
            left = dfs(root.left)
            right = dfs(root.right)
            
            #False
            if root.val == 0:
                return [1,0]
            #True
            elif root.val == 1:
                return [0,1]
            
            #OR
            elif root.val == 2:

                #True and True
                Tmin = min(Tmin, left[0] + right[0])
                
                #False and True
                Tmin = min(Tmin, left[1] + right[0])
                
                #True and False
                Tmin = min(Tmin, left[0] + right[1])
                    
                #False + False
                Fmin = min(Fmin, left[1] + right[1])
                
                     
            #AND    
            elif root.val == 3:
                #True + True
                Tmin = min(Tmin, left[0] + right[0])

                #True + False
                Fmin = min(Fmin, left[0] + right[1])
                
                #False + True
                Fmin = min(Fmin, left[1] + right[0])
                
                #False + False
                Fmin = min(Fmin, left[1] + right[1])

            #XOR
            elif root.val == 4:
                
                #False + True
                Tmin = min(Tmin, left[1] + right[0])
                
                #True + False
                Tmin = min(Tmin, left[0] + right[1])
    
                #False + False
                Fmin = min(Fmin, left[1] + right[1])
                
                #True + True
                Fmin = min(Fmin, left[0] + right[0]) 
            
            #NOT
            else:
                Tmin = min(Tmin, left[1] + right[1])
                Fmin = min(Fmin, left[0] + right[0])
            
            return [Tmin,Fmin]
        
        
        res = dfs(root)
        
        if result:
            return res[0]
        else:
            return res[1]
