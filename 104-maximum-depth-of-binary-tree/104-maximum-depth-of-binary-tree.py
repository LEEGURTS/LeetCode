# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        result = []
        def findDepth(r,depth=1):
            if r is None:
                return depth
            result.append(depth)
            findDepth(r.left,depth+1)
            findDepth(r.right,depth+1)
        findDepth(root)
        if len(result) == 0:
            return 0
        return max(result)