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
        #map out all of the values for inorder first to save time searching
        for i in range(len(inorder)):
            
            keyidx[inorder[i]] = i
 
    
        #we will use post order for our middle nodes and each time we will decrement to get a new middle node.. this will help us keep track
        index = len(postorder)
        
        def dfs(l,r):
            nonlocal index
            
            #left is bigger than right?
            if l > r:
                return
            #decrement our middle node
            index -=1
            val = postorder[index]
            #create a new node with middle value
            root = TreeNode(val)
            
            #find the middle in our inorder so that left of this value is our left subtree and right of this value is our right subtree
            mid = keyidx[val]
            
            #build our right than our left since the postorder backwards goes right first
            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid -1)
    
            return root
        
        
        return dfs(0, index -1)
        