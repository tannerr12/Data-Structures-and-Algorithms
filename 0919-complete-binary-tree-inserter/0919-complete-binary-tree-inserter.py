# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque([[root, None]])
        seenNone = False
        #gather all the nodes from the layer with a missing value
        while self.q and seenNone == False:
            
            for i in range(len(self.q)):
                
                node,par = self.q.popleft()
                
                if node.left:
                    self.q.append([node.left, node])
                else:
                    seenNone = True
                    self.q.append([None, node])
                if node.right:
                    self.q.append([node.right, node])
                else:
                    seenNone = True
                    self.q.append([None, node])
        
                        
        
        

    def insert(self, val: int) -> int:
        
        
        
        while True:
            node,par = self.q.popleft()
            
            if node != None:
                self.q.append([None, node])
                self.q.append([None, node])
            else:
                if not par.left:
                    par.left = TreeNode(val)
                    self.q.append([None, par.left])
                    self.q.append([None, par.left])
                    return par.val
                    
                else:
                    par.right = TreeNode(val)
                    self.q.append([None, par.right])
                    self.q.append([None, par.right])
                    return par.val                    
        
        
    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()