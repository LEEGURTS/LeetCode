
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
                result.append(depth)
                return

            finddepth(node.left, depth+1)
            finddepth(node.right, depth+1)
            
        finddepth(root,1)
        if len(result) == 0:
            return 0
        return max(result) - 1