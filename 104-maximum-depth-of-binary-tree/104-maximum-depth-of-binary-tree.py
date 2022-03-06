
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        result = []
        
        def finddepth(node: TreeNode, depth):
            if not node:
                return
            result.append(depth)
            if node.left:
                finddepth(node.left, depth+1)
            if node.right:
                finddepth(node.right, depth+1)
            
        finddepth(root,1)
        if len(result) == 0:
            return 0
        return max(result)