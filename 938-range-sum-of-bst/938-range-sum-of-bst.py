class Solution:
    result : int = 0 
    def rangeSumBST(self, root:TreeNode, low: int, high: int) -> int:
        def finder(node:TreeNode):
            if node:
                if low <= node.val <= high:
                    self.result += node.val
                finder(node.left)
                finder(node.right)
        finder(root)
        return self.result