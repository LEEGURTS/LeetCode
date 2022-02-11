class Solution:
    val : int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                dfs(node.right)
                self.val += node.val
                node.val = self.val
                dfs(node.left)
        dfs(root)
        return root