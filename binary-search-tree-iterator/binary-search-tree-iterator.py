# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
       
        self.stack = []
        def dfs(root):
            if root is None:
                return 
            
            dfs(root.left)
            self.stack.append(root.val)
            dfs(root.right)
        
        dfs(root)
        self.idx = 0
    def next(self) -> int:
        res = self.stack[self.idx]
        self.idx +=1
        return res
            

    def hasNext(self) -> bool:
        if self.idx < len(self.stack):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()