# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #both start at the far left
        #post order ends at the root
        #post order is preorder backwards
        
        
        keyidx = {}
        
        for i in range(len(inorder)):
            
            keyidx[inorder[i]] = i
            
        
        index = len(postorder)
        def dfs(l,r):
            nonlocal index
            if l > r:
                return
            
            index -=1
            val = postorder[index]
            root = TreeNode(val)
            
            mid = keyidx[val]
            
            
            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid -1)
            
            
            
            return root
        
        
        return dfs(0, index -1)
        