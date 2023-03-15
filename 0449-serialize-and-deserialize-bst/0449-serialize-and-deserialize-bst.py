# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        st = ''
        
        def dfs(root):
            nonlocal st
            if not root:
                return None
            
            st += str(root.val) + ','
            
            dfs(root.left)
            dfs(root.right)
        
        
        dfs(root)
        #print(st)
        return st
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = data[:-1]
        arr = data.split(',')
        print(arr)
        if arr[0] == '':
            arr.pop(0)
        def dfs(arr, lower,higher):
            if not arr:
                return None
            if int(arr[0]) <= higher and int(arr[0]) >= lower:
                
                cand = arr.pop(0)
                cand = int(cand)
                node = TreeNode(int(cand))
                
                node.left = dfs(arr,lower,cand)
                node.right = dfs(arr,cand, higher)
                
                return node
            
            else:
                return None
            
        
        return dfs(arr,float('-inf'), float('inf'))
                
            

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans