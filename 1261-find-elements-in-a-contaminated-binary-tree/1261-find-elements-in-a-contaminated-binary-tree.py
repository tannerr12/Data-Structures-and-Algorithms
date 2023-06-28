# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.nRoot = self.dfs(root) 
        self.s = set()
        self.search(root)
    
    def search(self, node):
        if node is None:
            return None
        
        self.s.add(node.val)
        self.search(node.left)
        self.search(node.right)
        
    def dfs(self, node):
        if node is None:
            return None
        
        val = node.val
        
        if node.left != None:
            node.left.val = 2 * val + 1
            self.dfs(node.left)
        if node.right != None:
            node.right.val = 2 * val + 2
            self.dfs(node.right)
        
        
        return node
        

    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)