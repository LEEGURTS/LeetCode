
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val+root2.val)
            node.left, node.right = self.mergeTrees(root1.left,root2.left),self.mergeTrees(root1.right,root2.right)

            return node
        else:
            return root1 or root2