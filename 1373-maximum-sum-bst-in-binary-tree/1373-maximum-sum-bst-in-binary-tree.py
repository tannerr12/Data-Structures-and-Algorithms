# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            
            if not node:
                return [0, True, 0, float('inf'), -float('inf')]
            
            totalL, isBSTL,bestL,mnl,mxl = dfs(node.left)
            totalR, isBSTR,bestR,mnr,mxr = dfs(node.right)

            if isBSTL and isBSTR and node.val > mxl and node.val < mnr:
                if node.left and node.right:
                    if node.left.val < node.val and node.val < node.right.val:
                        return [totalL + totalR + node.val,True, max(bestL,bestR, node.val + totalL + totalR), min(mnl, node.val), max(mxr, node.val)]
                elif node.left:
                    if node.left.val < node.val:
                        return [totalL + totalR + node.val,True, max(bestL,bestR, node.val + totalL + totalR), min(mnl, node.val), max(mxr, node.val)]

                elif node.right:
                    if node.right.val > node.val:
                        return [totalL + totalR + node.val,True, max(bestL,bestR, node.val + totalL + totalR), min(mnl, node.val), max(mxr, node.val)]

                else:
                    return [totalL + totalR + node.val,True, max(bestL,bestR, node.val + totalL + totalR), min(mnl, node.val), max(mxr, node.val)]
            
            
            return [0,False,max(bestL,bestR), min(mnl, node.val), max(mxr, node.val)]
        
        val = dfs(root)
        
        return val[2]